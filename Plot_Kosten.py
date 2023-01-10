import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.ticker as tkr

def fmt(x, pos):
        s = '{}'.format(int(x/1000000000)) + ' Mrd'
        return s
    
conn = sqlite3.connect('Data.db')
c = conn.cursor()

data = pd.read_sql_query('SELECT * FROM Simulationen_2_2021', conn)
data = data[data['Brennstoffzellen_Anzahl'] != 4500000]
data = data[data['Deckung'] > 70]      
  
c.close()
conn.close()

plt.style.use('seaborn')
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

ax.scatter(data['Deckung'], data['Kosten'], s=10, marker='.', edgecolors='b')

ax.yaxis.set_major_formatter(tkr.FuncFormatter(fmt))

ax.set_xlabel('Deckung in %')
ax.set_ylabel('Kosten in Euro')

plt.show()

