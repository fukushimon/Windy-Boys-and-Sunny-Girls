import pandas as pd
import sqlite3

conn = sqlite3.connect('Data.db')
c = conn.cursor()

#Viertelstundendaten HH
df = pd.read_csv('Data/HH.csv', sep=';')
df.to_sql('HH', con=conn, if_exists='replace')

# Viertelstundendaten SH
df = pd.read_csv('Data/SH.csv', sep=';')
df.to_sql('SH', con=conn, if_exists='replace')

# Gloablstrahlung 10-minütig, in W/m^2
df = pd.read_csv('Data/Globalstrahlung.csv', sep=';')
df.to_sql('Globalstrahlung', con=conn, if_exists='replace')

# Windgeschwindigkeiten in m/s in 130m Höhe
df = pd.read_csv('Data/Windgeschwindigkeiten.csv', sep=';')
df.to_sql('Windgeschwindigkeiten', con=conn, if_exists='replace')

# Leistung der WEA in kW bei unterschiedlichen Windstärken in m/s
df = pd.read_csv('Data/WEAs.csv', sep=';')
df.to_sql('WEAs', con=conn, if_exists='replace')

# Nenndaten der PV-Module
df = pd.read_csv('Data/Solarmodule.csv', sep=';')
df.to_sql('Solarmodule', con=conn, if_exists='replace') 

# Test


c.close()
conn.close()



