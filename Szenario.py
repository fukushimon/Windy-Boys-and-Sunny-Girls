import pandas as pd
import sqlite3
from datetime import date

from Plots import Strommix, Wind, Globalstrahlung
from Anlagen import WEA, PVA, Akku, Pumpspeicher

class Szenario:
    wea_models = []
    pv_models = []
    
    def __init__(self, name, year, weather_year, last_szenario, wea_models, wea_count, wea_locations, pv_models, pv_area, pv_locations):
        self.name = name
        self.year = year
        self.weather_year = weather_year
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
        
        c.close()
        conn.close()
        
    def return_from_sql(self):
        conn = sqlite3.connect('Data.db')
        sql_query = pd.read_sql_query ('Szenarien', conn)

        df = pd.DataFrame(sql_query, columns = ['Datum','WEA_Modelle', 'WEA_Anzahl', 'WEA_Anzahl','PV_Fläche', 'PV_Modelle', 'PV_Standorte'])
      
        conn.close()
    
    def print_config(self):
        print(self.config)
    
    def calc_strommix(self):
        new_strommix = Strommix(self.last_szenario, self.year)
        
        # Calculate wind and solar for 2021
        v_wind = Wind(self.weather_year)
        rad_pv = Globalstrahlung(self.year, self.weather_year)
        
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

        total_energy_pv.index = total_energy_pv.index + pd.offsets.DateOffset(years = 2021 - self.weather_year)
        total_energy_wind.index = total_energy_wind.index + pd.offsets.DateOffset(years = 2021 - self.weather_year)
        
        new_strommix.add_to_wind_onshore(total_energy_wind)
        new_strommix.add_to_pv(total_energy_pv)
        
        return new_strommix
    
    def calc_bilanz(self):
        # Create Akku modules
        akku1 = Akku(20000, 0.95, 'Hamburg')
        pump1 = Pumpspeicher('Hamburg')
        
        bilanz = self.calc_strommix().calc_bilanz_ee('Both')
        
        def speicher(val):
            # Charge
            if val >= 0:
                if pump1.capacity_left() == 0:
                    diff = val - akku1.capacity_left()
                    if diff >= 0:
                        akku1.charge(akku1.capacity_left())
                        val = diff
                    elif diff < 0:
                        akku1.charge(val)
                        val = 0
                else:
                    diff = val - pump1.capacity_left()
                    if diff > 0:
                        pump1.charge(pump1.capacity_left())
                        val = diff
                        speicher(val)
                    elif diff <= 0:
                        pump1.charge(val)
                        val = 0
            else:
                if val > -400 and val < 0:
                    diff = abs(val) - pump1.capacity_left()
                    if diff > 0:
                        pump1.decharge(pump1.current_charge)
                        val = diff
                    elif diff <= 0:
                        pump1.decharge(abs(val))
                        val = 0
                else:
                    diff = abs(val) - (pump1.capacity_left() + akku1.capacity_left())
                    if diff > 0:
                        pump1.decharge(pump1.current_charge)
                        akku1.decharge(akku1.current_charge)
                        val = diff
                    elif diff <= 0:
                        pump1.decharge(400)
                        akku1.decharge(abs(val) - 400)
                        val = 0
                
                        
                        
            if val > 0 and val >= akku1.capacity_left():
                akku1.charge(akku1.capacity_left())
                val = val - akku1.capacity_left()
            elif val > 0 and val < akku1.capacity_left():
                akku1.charge(val)
                val = 0
            # Decharge
            elif val < 0 and abs(val) <= akku1.current_charge:
                akku1.decharge(abs(val))
                val = 0
            elif val < 0 and abs(val) > akku1.current_charge:
                akku1.decharge(akku1.current_charge)
                val = val + akku1.current_charge
            
            return pd.Series([val, akku1.current_charge])
            
        bilanz[['Bilanz_Neu', 'Speicher']] = bilanz['Bilanz'].apply(speicher)
        
        return bilanz