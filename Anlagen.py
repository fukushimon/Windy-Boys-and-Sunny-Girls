import pandas as pd
import sqlite3

class WEA:
    def __init__(self, manufacturer):
        self.connect_to_sql()
        
        self.manufacturer = manufacturer
        
        # Kosten der WEA???
        if self.manufacturer == 'Nordex':
            self.cost = 1000000 * 3.6 # 1000 Euro pro Kilowatt
        if self.manufacturer == 'Vestas':
            self.cost = 1000000 * 8
        if self.manufacturer == 'Senvion':
            self.cost = 1000000 * 3.4
        if self.manufacturer == 'GE':
            self.cost = 1000000 * 3.4
        if self.manufacturer == 'Gamesa':
            self.cost = 1000000 * 5
        if self.manufacturer == 'Enercon':
            self.cost = 1000000 * 4.2

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
        self.area = data_list[0][4]
        self.max_pwr = data_list[0][5]
        self.cost = 1.35 * self.max_pwr
        
        self.disconnect_from_sql()
        
    def connect_to_sql(self):
        self.conn = sqlite3.connect('Data.db')
        self.c = self.conn.cursor()
    
    def disconnect_from_sql(self):
        self.c.close()
        self.conn.close()

# WIrkungsgrade der Speicher berücksichtigen!!
class Speicher:
    def __init__(self, efficiency):
        self.efficiency = efficiency
        
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
        if self.current_charge >= (amount * (1 + self.efficiency)):
            self.current_charge = self.current_charge - amount * (1 + self.efficiency)
            return amount
        else:
            discharged_amount = self.current_charge * self.efficiency
            self.current_charge = 0
            return discharged_amount
    
    def capacity_left(self):
        return self.capacity - self.current_charge

class Akku(Speicher):
    def __init__(self, num_modules, start_charge, location):
        self.num_modules = num_modules
        super().__init__(0.9)
        self.power = 5 * num_modules # MW
        self.full_load_time = 1 # h
        self.capacity = self.power * self.full_load_time # MWh
        self.size = 50 * num_modules # m^2
        self.cost = 100000 * self.capacity # Euro
        self.current_charge = self.capacity * start_charge # MWh
        self.location = location

class Pumpspeicher(Speicher):
    def __init__(self, num_units, start_charge, location):
        super().__init__(0.8)
        self.power = 120 * num_units # MW
        self.full_load_time = 5 # h
        self.capacity = self.power * self.full_load_time # MWh
        self.current_charge = self.capacity * start_charge # MWh
        #self.size = 0 * num_units # to be determined
        self.cost = 0 * self.capacity # to be determined
        self.location = location

class Druckluftspeicher(Speicher):
    def __init__(self, num_units, start_charge, location):
        super().__init__(0.42)
        self.power = 321 * num_units # MW
        self.full_load_time = 5 # h
        self.capacity = self.power * self.full_load_time # MWh
        self.current_charge = self.capacity * start_charge # MWh
        self.size = 0 * num_units # to be determined
        self.cost = 86000 * self.capacity # Euro
        self.location = location

class GuD():
    def __init__(self):
        self.efficiency = 0.45
        self.production = 59.406 # MWh pro 15min
        
class Gasnetz():
    def __init__(self, num_elektrolyseure, start_charge):
        self.capacity = 0 # MWh
        self.current_charge = self.capacity * start_charge
        self.elec = Elektrolyseur(num_elektrolyseure)
        self.gud = GuD()
        self.cost = self.elec.cost

    def charge(self, amount):
        amount = amount * self.elec.efficiency
        if amount > self.elec.capacity:
            self.current_charge = self.current_charge + self.elec.capacity
            return self.elec.capacity
        else:
            self.current_charge = self.current_charge + amount
            return amount
    
    def discharge(self, amount):
        amount = amount * self.gud.efficiency
        if amount > self.current_charge:
            amount = self.current_charge
            
        if amount > self.gud.production:
            self.current_charge = self.current_charge - self.gud.production
            return self.gud.production
        else:
            self.current_charge = self.current_charge - amount
            return amount

class Elektrolyseur():
    def __init__(self, num_units):
        self.efficiency = 0.74
        self.power = 2 * num_units # MW
        self.capacity = 0.403 * num_units # MWh pro 15min
        #self.size = 0 * num_units # to be determined
        self.cost = 400000 * self.power # Euro
