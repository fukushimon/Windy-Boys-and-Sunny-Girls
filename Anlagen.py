import pandas as pd
import sqlite3

class WEA:
    def __init__(self, manufacturer):
        self.connect_to_sql()
        
        self.manufacturer = manufacturer
        
        # Kosten der WEA???
        self.cost = 0
        
        # Kennlinie der WEA 
        self.pwr_output = pd.read_sql_query(('SELECT Windgeschwindigkeit, {} FROM WEAs').format(manufacturer), self.conn)
        
        self.disconnect_from_sql()
        
    def connect_to_sql(self):
        self.conn = sqlite3.connect('Data.db')
        self.c = self.conn.cursor()
    
    def disconnect_from_sql(self):
        self.c.close()
        self.conn.close()

class PVA:
    def __init__(self, manufacturer):
        self.connect_to_sql()
        
        self.manufacturer = manufacturer
        
        self.c.execute(("SELECT * FROM Solarmodule WHERE Hersteller = '{}'").format(manufacturer))
        data_list = self.c.fetchall()
        
        self.efficiency = data_list[0][2]
        self.cost = data_list[0][3]
        self.area = data_list[0][4]
        self.max_pwr = data_list[0][5]
        
        self.disconnect_from_sql()
        
    def connect_to_sql(self):
        self.conn = sqlite3.connect('Data.db')
        self.c = self.conn.cursor()
    
    def disconnect_from_sql(self):
        self.c.close()
        self.conn.close()
    
class Speicher:
    def __init__(self):
        pass
        
    def get_charge_pct(self):
        return self.charge / self.capacity
    
    def charge(self, amount): # Returns the charged amount
        to_charge = self.capacity_left()
        if amount >= to_charge:
            self.current_charge = self.capacity
            return to_charge
        else:
            self.current_charge = self.current_charge + amount
            return amount
        
    def discharge(self, amount):
        if self.current_charge >= amount:
            self.current_charge = self.current_charge - amount
            return amount
        else:
            print("Error: Not enough charge!")
            discharged_amount = self.current_charge
            self.current_charge = 0
            return discharged_amount
    
    def capacity_left(self):
        return self.capacity - self.current_charge

class Akku(Speicher):
    def __init__(self, num_modules, start_charge, efficiency, location):
        self.num_modules = num_modules
        self.efficiency = efficiency 
        self.power = 5 * num_modules # MW
        self.capacity = self.power * 1 # MWh
        self.size = 50 * num_modules # m^2
        self.cost = 1200000 * self.capacity # Euro
        self.current_charge = self.capacity * start_charge # MWh
        self.location = location

class Pumpspeicher(Speicher):
    def __init__(self, num_units, start_charge, location):
        self.efficiency = 0.8
        self.power = 120 * num_units # MW
        self.capacity = self.power * 5 # MWh
        self.current_charge = self.capacity * start_charge # MWh
        self.size = 0 * num_units # to be determined
        self.cost = 0 * num_units # to be determined
        self.location = location

        