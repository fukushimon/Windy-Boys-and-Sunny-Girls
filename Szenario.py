import pandas as pd
import sqlite3
from datetime import date

from Plots import Strommix

class Szenario:
    def __init__(self, name, year, last_szenario, wea_models, wea_count, wea_locations, pv_models, pv_area, pv_locations):
        self.config = pd.DataFrame({
            'Datum': date.today(),
            'Jahr': year,
            'Last_Szenario': last_szenario,
            'WEA_Modelle': ','.join(map(str, wea_models)),
            'WEA_Anzahl': ','.join(map(str, wea_count)),
            'WEA_Standorte': ','.join(map(str, wea_locations)),
            'PV_Modelle': ','.join(map(str, pv_models)),
            'PV_Fläche': ','.join(map(str, pv_area)),
            'PV_Standorte': ','.join(map(str, pv_locations))
            }, index=[name])
        
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
        self.config.to_sql('Szenarien', conn, if_exists='replace')
        
        c.close()
        conn.close()
    
    def print_config(self):
        print(self.config)
    
    def calc_strommix(self):
        new_strommix = Strommix(self.year)
        
scene1 = Szenario('Test1', 2030, ['Gamesa', 'Enercon'], [200, 300], ['SPO', 'Hamburg'], ['SunPower'], [100], ['SPO'])
            
        