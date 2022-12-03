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
        self.pv_area = pv_area
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
        
        c.close()
        conn.close()
    
    def print_config(self):
        print(self.config)
    
    def calc_strommix(self):
        new_strommix = Strommix(3, self.year)
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
            'Modulflaeche': self.pv_area,
            'Standort': self.pv_locations
            })
        
        # Wind Erzeugung
        energy_wind = v_wind.data
        
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
        
        energy_wind.drop(energy_wind.columns[[0, 1, 2, 3, 4, 5, 6]], axis=1, inplace=True)
        
        # Solar Erzeugung
        energy_pv = rad_pv
        
        for index, row in pv.iterrows():
             # Globalstrahlung für den jeweiligen Standort
            list_rad = (rad_pv.data[('{}').format(row['Standort'])]).to_frame()
        
        return list_rad
        
        
scene1 = Szenario('Test1', 2030, 3, ['Nordex', 'Enercon'], [200, 300], ['SPO', 'Hamburg'], ['SunPower'], [100], ['SPO'])
wind = scene1.calc_strommix()
        