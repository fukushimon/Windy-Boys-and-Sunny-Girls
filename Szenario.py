import pandas as pd
import sqlite3
from datetime import date

class Szenario:
    
    def __init__(self, name, wea_models, wea_count, wea_locations, pv_models, pv_area, pv_locations):
        # self.name = name
        # self.wea_models = wea_models
        # self.wea_count = wea_count
        # self.wea_locations = wea_locations
        # self.pv_models = pv_models
        # self.pv_area = pv_area
        # self.pv_locations = pv_locations
        
        self.config = pd.DataFrame({
            'Datum': date.today(),
            'WEA_Modelle': ','.join(map(str, wea_models)),
            'WEA_Anzahl': ','.join(map(str, wea_count)),
            'WEA_Standorte': ','.join(map(str, wea_locations)),
            'PV_Modelle': ','.join(map(str, pv_models)),
            'PV_Fläche': ','.join(map(str, pv_area)),
            'PV_Standorte': ','.join(map(str, pv_locations))
            }, index=[name])
    
    def add_to_sql(self):
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        self.config.to_sql('Szenarien', conn, if_exists='replace')
        
        c.close()
        conn.close()
    
    def print_config(self):
        return self.config
            
        