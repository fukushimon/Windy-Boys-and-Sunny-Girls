import pandas as pd
import sqlite3
from datetime import date

from Plots import Strommix, Wind, Globalstrahlung
from Anlagen import WEA, PVA, Akku, Pumpspeicher, Druckluftspeicher, Gasnetz

class Szenario:    
    wind_repower = {
     'Anlagen': ['Enercon', 'Gamesa', 'Gamesa', 'Enercon', 'Gamesa', 'Gamesa', 'Enercon'],
     'Anzahl': [80, 10, 38, 5, 21, 73, 59],
     'Standorte': ['Schleswig', 'Fehmarn', 'Kiel', 'Schleswig', 'SPO', 'Leck', 'Quickborn']
     }
    
    def __init__(self, 
                 name, # Szenario-Name
                 year, # Szenario für welches Jahr: int
                 weather_year, # Wetterdaten aus welchem Jahr: 2020, 2021
                 last_szenario, # Welches Last Szenario: 1, 2, 3
                 repowering, # Wird Repowering berücksichtigt: True or False
                 wea_models, # Liste der WEA-Hersteller: String
                 wea_count, # Liste der WEA-Anzahl: int
                 wea_locations, # Liste der WEA-Standorte: String
                 pv_models, # Liste der PVA-Hersteller: String
                 pv_area, # Liste der PVA-Flächen: int
                 pv_locations, # Liste der PVA-Standorte: String
                 num_akku, # Anzahl der Akku-Module: int
                 num_pump, # Anzahl der Pumpspeicherkraftwerke: int
                 num_druckluft, # Anzahl der Druckluftspeicherkraftwerke: int
                 num_elektrolyseure, # Anzahl der Elektrolyseure: int
                 num_brennstoffzellen, # Anzahl der Brennstoffzellen
                 start_charge # Zu wie viel Prozent sich die Speicher am Anfang des Szenarios gefüllt?: float
                 ):
        
        self.wea_models = []
        self.pv_models = []
        self.pv_count = []
    
        self.name = name
        self.year = year
        self.weather_year = weather_year
        self.last_szenario = last_szenario
        self.repowering = repowering
        self.wea_count = wea_count
        self.wea_locations = wea_locations
        self.pv_area = pv_area # in km^2
        self.pv_locations = pv_locations
        self.num_akku = num_akku
        self.num_pump = num_pump
        self.num_druckluft = num_druckluft
        self.num_elektrolyseure = num_elektrolyseure
        self.num_brennstoffzellen = num_brennstoffzellen
        self.start_charge = start_charge
        
        for model in wea_models:
            self.wea_models.append(WEA(model))
        
        for model in pv_models:
            self.pv_models.append(PVA(model))
            
        if repowering == True:
            for model in self.wind_repower["Anlagen"]:
                self.wea_models.append(WEA(model))
            self.wea_count = self.wea_count + self.wind_repower["Anzahl"]
            self.wea_locations = self.wea_locations + self.wind_repower["Standorte"]
        
        for model, area in zip(self.pv_models, self.pv_area):
            self.pv_count.append(int(area * 40 / (model.max_pwr / 1000000)))
        
        # Create Speicher instances from user input
        self.akku = Akku(self.num_akku, self.start_charge, 'Quickborn')
        self.pump = Pumpspeicher(self.num_pump, self.start_charge, 'Quickborn')
        self.druckluft = Druckluftspeicher(self.num_druckluft, self.start_charge, 'Quickborn')
        self.gasnetz = Gasnetz(self.num_elektrolyseure, self.num_brennstoffzellen, self.start_charge)
        
        # Add to database
        self.add_to_sql()
        
        # Create Strommix
        self.strommix = self.calc_strommix()
    
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
        
        new_strommix.add_to_wind_onshore(total_energy_wind.round(3))
        new_strommix.add_to_pv(total_energy_pv.round(3))
        
        # Add Speicher columns
        speicher = self.calc_speicher(new_strommix)[['Pumpspeicher_Ladestand', 'Druckluftspeicher_Ladestand', 'Akku_Ladestand', 'Gasnetz_Fuellstand', 'Speicher']]
        new_strommix.add_speicher(speicher, 'SH')
        
        return new_strommix
    
    def calc_speicher(self, mix):        
        bilanz = mix.calc_bilanz_ee('Both')
        
        def speicher(val):
            if val >= 0: # Einspeicherung
                val = val - self.gasnetz.charge(val)
                if val > 0 and self.pump.capacity_left() == 0 and self.druckluft.capacity_left() == 0: 
                    val = val - self.akku.charge(val)
                elif val > 0:
                    val = val - self.pump.charge(val/2)
                    val = val - self.druckluft.charge(val)
                    if val > 0:
                        val = val - self.akku.charge(val)
            else: # Ausspeicherung
                val = val + self.gasnetz.discharge(abs(val))
                if val < 0:
                    while True:
                        val = val + self.pump.discharge(abs(val/2))
                        val = val + self.druckluft.discharge(abs(val))
                        
                        if ((self.pump.current_charge < abs(val)) and (self.druckluft.current_charge < abs(val))):
                            if(round(val, 3) >= 0):
                                val = 0
                            break
                        
                        if(round(val, 3) >= 0):
                            val = 0
                            break
                    
                    if val < 0:
                        val = val + self.akku.discharge(abs(val))
            
            return pd.Series([val, self.pump.current_charge, self.druckluft.current_charge, self.akku.current_charge, self.gasnetz.current_charge])
            
        bilanz[['Bilanz_Neu', 'Pumpspeicher_Ladestand', 'Druckluftspeicher_Ladestand', 'Akku_Ladestand', 'Gasnetz_Fuellstand']] = bilanz['Bilanz'].apply(speicher)
        bilanz['Speicher'] = bilanz['Bilanz_Neu'] - bilanz['Bilanz']
        bilanz['Speicher'].where(bilanz['Speicher'] > 0, 0, inplace=True)
        
        return bilanz
    
    def calc_cost(self):
        wea_costs = []
        for model, count in zip(self.wea_models, self.wea_count):
            wea_costs.append(model.cost*count)
            
        pva_costs = []
        for model, count in zip(self.pv_models, self.pv_count):
            pva_costs.append(model.cost*count)   
        
        speicher_costs = [self.akku.cost, self.pump.cost, self.druckluft.cost, self.gasnetz.cost]
        
        total_cost = sum(wea_costs) + sum(pva_costs) + sum(speicher_costs)
        
        return total_cost