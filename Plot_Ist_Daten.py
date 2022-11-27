import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
import datetime
from datetime import datetime
import seaborn as sns
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

class DataPlot:
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    
    def __init__(self):
        plt.style.use('seaborn')
        
    # Daten einlesen aus Datenbank; Gibt ein DataFrame zurück
    def get_data(self, type):
        if type == 'Globalstrahlung':
            df = pd.read_sql_query('SELECT * FROM Globalstrahlung', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format='%Y%m%d%H%M')
            df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
    
            # 10min-Daten in 15min-Daten umwandeln
            new_df = df.resample('15min').mean()
            
            return new_df
        
        elif type == 'Windgeschwindigkeiten':
            df = pd.read_sql_query('SELECT * FROM Windgeschwindigkeiten', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format='%Y%m%d%H%M')
            df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
    
            # 10min-Daten in 15min-Daten umwandeln
            new_df = df.resample('15min').mean()
            
            return new_df
        
        elif type == 'Strommix_HH':
            df = pd.read_sql_query('SELECT Datum, Last, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kernenergie, Kohle, Erdgas, Speicher, Sonstige_Konventionelle FROM HH', self.conn, index_col='Datum').loc['2021']
            df.index = pd.to_datetime(df.index, format="%d.%m.%y %H:%M")
            #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
            return df
        
        elif type == 'Strommix_SH':
            df = pd.read_sql_query('SELECT Datum, Last, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kernenergie, Kohle, Erdgas, Speicher, Sonstige_Konventionelle FROM SH', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")
            #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
            return df
        
        elif type == 'Strombilanz_HH':
            df = pd.read_sql_query('SELECT Datum, Last, Erzeugung FROM HH', self.conn, index_col='Datum').loc['2021']
            df.index = pd.to_datetime(df.index, format="%d.%m.%y %H:%M")
            #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
            return df
        
        elif type == 'Strombilanz_SH':
            df = pd.read_sql_query('SELECT Datum, Last, Erzeugung FROM SH', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")
            #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
            return df
        
        elif type == 'Solarmodule':
            df = pd.read_sql_query('SELECT * FROM Solarmodule', self.conn)
            return df
        
        elif type == 'WEAs':
            df = pd.read_sql_query('SELECT * FROM WEAs', self.conn, index_col='Windgeschwindigkeit')
            return df
        else:
            return None
    
    # Ermittelt das Mittel der Daten über mehrere Jahre (z.B. Globalstrahlung, Windgeschwindigkeiten oder Strommix HH)
    def calc_mean(self, data): 
        data_cpy = data.copy()
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2020
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M")) 
        
        # DataFrame gruppieren nach 'Datum_Normiert'
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        
        # Durchschnitt berechnen
        mean_df = year_grp.mean()
        
        # 'Datum_Normiert'-Spalte umbennen:
        mean_df.index.rename('Datum', inplace=True)
        
        return mean_df
    
    # Ermittelt das Mittel der Daten über mehrere Jahre (z.B. Globalstrahlung, Windgeschwindigkeiten oder Strommix HH)
    def calc_max(self, data):
        data_cpy = data.copy()
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M"))  
        year_grp = data_cpy.groupby(['Datum_Normiert']) 
        max_df = year_grp.max()
        max_df.index.rename('Datum', inplace=True)
        return max_df
    
    # Ermittelt das Mittel der Daten über mehrere Jahre (z.B. Globalstrahlung, Windgeschwindigkeiten oder Strommix HH)
    def calc_min(self, data):
        data_cpy = data.copy()
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M"))
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        min_df = year_grp.min()
        min_df.index.rename('Datum', inplace=True)
        return min_df
    
    # Berechnet den Gesamt-Stromverbrauch und Stromerzeugung im Jahr x
    def calc_total_consumption(self, year):
        data_HH = self.calc_mean(self.get_data('Strombilanz_HH'))
        data_SH = self.calc_mean(self.get_data('Strombilanz_SH'))
        
        # Aktueller Gesamtverbrauch in beiden Bundesländern
        data_total = data_HH + data_SH
        #data_total = data_total.to_frame()
        
        # Zukünftiger Gesamtverbrauch mit Faktor 1.02/Jahr
        data_total['Last_Prognose'] = data_total['Last'].apply(lambda row: row*pow(1.02, year-2022))
        
        return data_total
    
    # Berechnet die Globalstrahlung im Jahr x
    def calc_total_radiation(self, year):
        data = calc_mean(get_data('Globalstrahlung'))
        
        # Zukünftige Globalstrahlung mit Faktor 1.022/Jahr
        data_total = data.apply(lambda row: row*pow(1.022, year-2022))
        
        return data_total
    
    # Plottet die Strombilanz
    def plot_balance(self, consumption, production):
        cols = sns.color_palette("coolwarm", 2)
        
        # Berechnen der Strombilanz als Differenz aus Erzeugung und Last
        balance = production - consumption
        balance = balance.to_frame()
        balance.rename(columns={0: 'Bilanz'}, inplace=True)
        
        # Erstellen der x- und y-Arrays zum plotten
        x = mdates.date2num(balance.index) # Konvertiert das Datum in ein float (matplotlib kann nur mit floats arbeiten)
        y = balance['Bilanz'].to_numpy()
        
        # Erstellen des Plots (LineCollection); siehe: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
        fig, ax = plt.subplots()
        
        cmap = ListedColormap([cols[1], cols[0]])
        norm = BoundaryNorm([-1000, 0, 1000], cmap.N)
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(y)
        lc.set_linewidth(1)
        line = ax.add_collection(lc)
        
        hfmt = mdates.DateFormatter('%b')
        ax.xaxis.set_major_formatter(hfmt)
        ax.xaxis.set_major_locator(mdates.MonthLocator())
    
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(-1500, 1500)
        plt.show()
        
        # Wie viel Prozent der Viertelstunden ist gedeckt?
        filt = balance['Bilanz'] >= 0 
        positive_balance = balance[filt] # Liste aller Viertelstunden an denen die Bilanz positiv ist
        
        # In Prozent
        print(positive_balance.size / len(balance.index) * 100)
        
        return fig
    
    # custom formatter function: Energy shall be displayed as MWh
    def energy_numfmt(self, x, pos):
        s = '{}'.format(x.astype(int)) + ' MWh'
        return s
    
    # Plottet den Strommix
    def plot_energy_mix(self, data):
        cols = sns.color_palette("Spectral", 11)
        fig, ax = plt.subplots()
        
        ax.stackplot(data.index, data['Biomasse'], data['Wasserkraft'], data['Wind_Offshore'], data['Wind_Onshore'], data['Photovoltaik'], data['Sonstige_Erneuerbare'], data['Speicher'], colors=cols, labels=list(data.columns)[1:])
        ax.plot(data.index, data['Last'], label='Last', alpha=0.5)
        
        ax.legend(loc='upper left', frameon=1)
        
        hfmt = mdates.DateFormatter('%b')
        ax.xaxis.set_major_formatter(hfmt)
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        return fig
    
    def calc_balance_renewables(self):
        data_hh = self.get_data_renewables('Strommix_HH').loc['2021']
        data_sh = self.get_data_renewables('Strommix_SH')
        
        data_total = data_hh + data_sh
        data_total['Erzeugung_EE'] = data_total['Biomasse'] + data_total['Wasserkraft'] + data_total['Wind_Offshore'] + data_total['Wind_Onshore'] + data_total['Photovoltaik'] + data_total['Sonstige_Erneuerbare'] + data_total['Speicher']
        
        return data_total
    
    # Liest Strommix ein (berücksichtigt nur Erneuerbare)
    def get_data_renewables(self, type):
        if type == 'Strommix_HH':
            df = pd.read_sql_query('SELECT Datum, Last, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Speicher FROM HH', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format="%d.%m.%y %H:%M")
            return df
        
        elif type == 'Strommix_SH':
            df = pd.read_sql_query('SELECT Datum, Last, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Speicher FROM SH', self.conn, index_col='Datum')
            df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")
            return df
        
        else:
            return None



#df = calc_mean(get_data('Strombilanz_HH'))
# hh_bilanz = plot_balance(df['Last'], df['Erzeugung'])

#df2 = get_data('Strombilanz_SH')
#sh_bilanz = plot_balance(df2['Last'], df2['Erzeugung'])

#df3 = calc_total_consumption(2022)
#gesamt = plot_balance(df3['Last_Prognose'], df3['Erzeugung'])

# Plotten der Strombilanz nur mit Erneuerbaren Energien
# total_balance = calc_balance_renewables()
# plot_balance(total_balance['Last'], total_balance['Erzeugung_EE'])

# # HH Strommix (2021)
# hh = get_data_renewables('Strommix_HH').loc['2021']

# # SH Strommix
# sh = get_data_renewables('Strommix_SH')

# # Gesamt Strommix
# total = hh + sh

# plot_energy_mix(hh)
# plot_energy_mix(sh)
# plot_energy_mix(total)

# c.close()
# conn.close()