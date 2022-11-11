import pandas as pd
import sqlite3

conn = sqlite3.connect('HH_Data.db')
c = conn.cursor()

# Viertelstundendaten HH
df = pd.read_excel('C:/Users/shimo/Desktop/IPJ_Repository/Windy-Boys-and-Sunny-Girls/Data/HH_2020.xlsx')
df.to_sql('HH_2020', con=conn, if_exists='replace')

df = pd.read_excel('C:/Users/shimo/Desktop/IPJ_Repository/Windy-Boys-and-Sunny-Girls/Data/HH_2021.xlsx')
df.to_sql('HH_2021', con=conn, if_exists='replace')

df = pd.read_excel('C:/Users/shimo/Desktop/IPJ_Repository/Windy-Boys-and-Sunny-Girls/Data/HH_2022.xlsx')
df.to_sql('HH_2022', con=conn, if_exists='replace')

df = pd.read_excel('C:/Users/shimo/Desktop/IPJ_Repository/Windy-Boys-and-Sunny-Girls/Data/SH_2021.xlsx')
df.to_sql('SH_2021', con=conn, if_exists='replace')

c.close()
conn.close()



