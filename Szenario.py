import pandas as pd
import sqlite3
from datetime import date

from Plots import Strommix, Wind, Globalstrahlung

class Szenario:
    def __init__(self, name, year, last_szenario, wea_models, wea_count, wea_locations, pv_models, pv_area, pv_locations):
        self.name = name
        self.year = year
        self.last_szenario = last_szenario
        self.wea_models = wea_models
        self.wea_count = wea_count
        self.wea_locations = wea_locations
        self.pv_models = pv_models
        self.pv_area = pv_area
        self.pv_locations = pv_locations
        
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
        for index, row in wind.iterrows():
            # Windgeschwindigkeiten für den jeweiligen Standort
            list_wind = v_wind.data[('{}').format(row['Standort'])]
            print(list_wind)
        
        
scene1 = Szenario('Test1', 2030, 3, ['Gamesa', 'Enercon'], [200, 300], ['SPO', 'Hamburg'], ['SunPower'], [100], ['SPO'])
wind = scene1.calc_strommix()
        