import pandas as pd
import sqlite3
from datetime import date

from Plots import Strommix, Wind, Globalstrahlung
from Anlagen import WEA, PVA

class Szenario:
    wea_models = []
    pv_models = []
    
    def __init__(self, name, year, last_szenario, wea_models, wea_count, wea_locations, pv_models, pv_area, pv_locations):
        self.name = name
        self.year = year
        self.last_szenario = last_szenario
        self.wea_count = wea_count
        self.wea_locations = wea_locations
        self.pv_area = pv_area # in km^2
        self.pv_locations = pv_locations
        
        for model in wea_models:
            self.wea_models.append(WEA(model))
        
        for model in pv_models:
            self.pv_models.append(PVA(model))
        
        # Add to database
        self.add_to_sql()
    
    def add_to_sql(self):
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        
        params = pd.DataFrame({
            'Datum': date.today(),
            'Jahr': self.year,
            'Last_Szenario': self.last_szenario,
            'WEA_Modelle': ','.join(map(str, self.wea_models)),
            'WEA_Anzahl': ','.join(map(str, self.wea_count)),
            'WEA_Standorte': ','.join(map(str, self.wea_locations)),
            'PV_Modelle': ','.join(map(str, self.pv_models)),
            'PV_Flaeche': ','.join(map(str, self.pv_area)),
            'PV_Standorte': ','.join(map(str, self.pv_locations))
        }, index=[self.name])
        
        params.to_sql('Szenarien', conn, if_exists='replace')

        self.config.to_sql('Szenarien', conn, if_exists='append')

        
        c.close()
        conn.close()
    
    def print_config(self):
        print(self.config)
    
    def calc_strommix(self):
        new_strommix = Strommix(self.last_szenario, self.year)
        v_wind = Wind('mean')
        rad_pv = Globalstrahlung(self.year, 'mean')
        
        # Wind
        wind = pd.DataFrame({
            'Modell': self.wea_models,
            'Anzahl': self.wea_count,
            'Standort': self.wea_locations
            })
        
        # PV
        pv = pd.DataFrame({
            'Modell': self.pv_models,
            'Flaeche': self.pv_area,
            'Standort': self.pv_locations
            })
        
        # Wind Erzeugung
        energy_wind = v_wind.data.drop(v_wind.data.columns[[0, 1, 2, 3, 4, 5, 6]], axis=1)
        
        for index, row in wind.iterrows():
            # Windgeschwindigkeiten für den jeweiligen Standort
            list_wind = (v_wind.data[('{}').format(row['Standort'])]).to_frame()
            
            # Match Windgeschwindigkeiten from list_wind to Power from WEA
            merged_df = pd.merge(list_wind, row['Modell'].pwr_output, how='left', left_on = row['Standort'], right_on = 'Windgeschwindigkeit').set_axis(list_wind.index)  
            
            # Multiply by nnumber of WEAs/4000 (in MWh)
            merged_df[row['Modell'].manufacturer] = merged_df[row['Modell'].manufacturer].multiply(row['Anzahl']/4000)
            
            # Remove unneeded columns
            merged_df.drop(merged_df.columns[[0, 1]], axis=1, inplace=True)
            
            # Concat to energy_wind dataframe
            energy_wind = pd.concat([energy_wind, merged_df], axis=1)
        
        # Solar Erzeugung
        energy_pv = rad_pv.data.drop(rad_pv.data.columns[[0, 1, 2, 3]], axis=1)
        
        for index, row in pv.iterrows():
            module = row['Modell']
            pr_factor = 0.7
            
            # Globalstrahlung für den jeweiligen Standort
            list_rad = (rad_pv.data[('{}').format(row['Standort'])]).to_frame()
            
            # Total number of pv modules
            number_pv = row['Flaeche'] * 40 / (module.max_pwr / 1000000)
            
            # Power output for one pv module and convert to MWh
            list_rad = list_rad * module.efficiency * module.area * pr_factor / 4000000
            
            # Multiply with total number of pv modules
            list_rad = list_rad * number_pv
            
            # Concat to energy_pv dataframe
            energy_pv = pd.concat([energy_pv, list_rad], axis=1)
            
        # Total energy 
        total_energy_wind = energy_wind.sum(axis=1)
        total_energy_pv = energy_pv.sum(axis=1)
        
        #total_energy_wind.rename(columns={0: 'Wind_Onshore_Neu'}, inplace=True)
        #total_energy_pv.rename(columns={0: 'Photovoltaik_Neu'}, inplace=True)
        
        # Add to Strommix
        # new_strommix.sh_data = pd.concat([new_strommix.sh_data, total_energy_wind, total_energy_pv], axis=1, join='inner')
        # new_strommix.sh_data 
        
        new_strommix.add_to_wind_onshore(total_energy_wind)
        new_strommix.add_to_pv(total_energy_pv)
        
        return new_strommix
        

wind = {
    'Anlagen': ['Gamesa', 'Enercon', 'Gamesa', 'Gamesa', 'Enercon', 'Enercon', 'Enercon', 'Enercon', 'Enercon'],
    'Anzahl': [24, 126, 21, 1, 72, 49, 4, 6, 42],
    'Standorte': ['Leck', 'Schleswig', 'Kiel', 'Kiel', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn']
    }
        
solar = {
    'Anlagen': ['SunPower', 'SunPower', 'SunPower'],
    'Flaeche': [125, 243, 80],
    'Standorte': ['Schleswig', 'SPO', 'Leck']
    }

scene1 = Szenario('Test1', 2100, 1, wind['Anlagen'], wind['Anzahl'], wind['Standorte'], solar['Anlagen'], solar['Flaeche'], solar['Standorte'])
scene1_strommix = scene1.calc_strommix()
scene1_strommix.plot_bilanz_ee('Both')
bilanz = scene1_strommix.calc_bilanz_ee('Both')
print(scene1_strommix.calc_pct_positive_bilanz(bilanz))