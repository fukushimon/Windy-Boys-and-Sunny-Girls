# import matplotlib
# matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
import datetime
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
#import datetime
from datetime import datetime, timedelta
import seaborn as sns
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

class Plot:
    def __init__(self, tablename):
        pass
    
    def connect_to_sql(self):
        self.conn = sqlite3.connect('Data.db')
        self.c = self.conn.cursor()
    
    def disconnect_from_sql(self):
        self.c.close()
        self.conn.close()
        
    # custom formatter function: Energy shall be displayed as MWh
    def energy_numfmt(self, x, pos):
        s = '{}'.format(x.astype(int)) + ' MWh'
        return s

class Strommix(Plot):
    def __init__(self):
        self.connect_to_sql()
        
        # Hamburg Data
        self.hh_data = pd.read_sql_query('SELECT * FROM HH', self.conn, index_col='Datum')
        self.hh_data.drop('index', axis=1, inplace=True)
        self.hh_data.index = pd.to_datetime(self.hh_data.index, format="%d.%m.%Y %H:%M")
        
        # Schleswig Holstein Data
        self.sh_data = pd.read_sql_query('SELECT * FROM SH', self.conn, index_col='Datum')
        self.sh_data.drop('index', axis=1, inplace=True)
        self.sh_data.index = pd.to_datetime(self.sh_data.index, format="%d.%m.%Y %H:%M")
        
        # Sum of both
        self.both_data = self.hh_data + self.sh_data
        
        self.disconnect_from_sql()
    
    def plot_strommix(self, location):
        if location == 'HH':
            data_to_plot = self.hh_data.loc['2021']
        elif location == 'SH':
            data_to_plot = self.sh_data.loc['2021']
        elif location == 'Both':
            data_to_plot = self.both_data.loc['2021']
            
        data_to_plot.drop('Erzeugung', axis=1, inplace=True)
        
        plt.style.use('seaborn')
        cols = sns.color_palette("Spectral", 11)
        
        fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
        ax.stackplot(data_to_plot.index, (data_to_plot.reset_index(drop=True)).drop('Last', axis=1).T, colors=cols, labels=list(data_to_plot.columns)[1:])
        #ax.plot(data_to_plot.index, data_to_plot['Last'], label='Last', alpha=0.6, color='crimson', linewidth=1)
        
        ax.legend(loc='upper left', frameon=1)
        
        hfmt = mdates.DateFormatter('%b')
        ax.xaxis.set_major_formatter(hfmt)
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        plt.show()
        
        return fig
    
    def plot_strommix_ee(self, location):
        if location == 'HH':
            data_to_plot = self.hh_data.loc['2021']
        elif location == 'SH':
            data_to_plot = self.sh_data.loc['2021']
        elif location == 'Both':
            data_to_plot = self.both_data.loc['2021']
        
        data_to_plot.drop(['Erzeugung', 'Kernenergie', 'Kohle', 'Erdgas', 'Sonstige_Konventionelle'], axis=1, inplace=True)
            
        plt.style.use('seaborn')
        cols = sns.color_palette("Spectral", 11)
        
        fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
        ax.stackplot(data_to_plot.index, (data_to_plot.reset_index(drop=True)).drop('Last', axis=1).T, colors=cols, labels=list(data_to_plot.columns)[1:])
        #ax.plot(data_to_plot.index, data_to_plot['Last'], label='Last', alpha=0.6, color='crimson', linewidth=1)
        
        ax.legend(loc='upper left', frameon=1)
        
        hfmt = mdates.DateFormatter('%b')
        ax.xaxis.set_major_formatter(hfmt)
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        plt.show()
        
        return fig    
    
    def calc_erzeugung_ee(self, location):
        list_of_ee = ['Biomasse', 'Wasserkraft', 'Wind_Offshore', 'Wind_Onshore', 'Photovoltaik', 'Sonstige_Erneuerbare', 'Speicher']
        
        if location == 'HH':
            erzeugung = self.hh_data[list_of_ee].sum(axis=1)
        elif location == 'SH':
            erzeugung = self.sh_data[list_of_ee].sum(axis=1)
        elif location == 'Both':
            erzeugung = self.both_data[list_of_ee].sum(axis=1)
        
        return erzeugung
    
    def calc_bilanz(self, location):
        if location == 'HH':
            bilanz = self.hh_data['Erzeugung'].loc['2021'] - self.hh_data['Last'].loc['2021'] 
        elif location == 'SH':
           bilanz = self.sh_data['Erzeugung'].loc['2021'] - self.sh_data['Last'].loc['2021'] 
        elif location == 'Both':
            bilanz = self.both_data['Erzeugung'].loc['2021'] - self.both_data['Last'].loc['2021'] 
        
        bilanz = bilanz.to_frame()
        bilanz.rename(columns={0: 'Bilanz'}, inplace=True)
        
        return bilanz
    
    def calc_bilanz_ee(self, location):
        if location == 'HH':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.hh_data['Last'].loc['2021'] 
        elif location == 'SH':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.sh_data['Last'].loc['2021'] 
        elif location == 'Both':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.both_data['Last'].loc['2021'] 
        
        bilanz = bilanz.to_frame()
        bilanz.rename(columns={0: 'Bilanz'}, inplace=True)
        
        return bilanz
    
    def calc_pct_positive_bilanz(self, bilanz):
        filt = filt = bilanz['Bilanz'] >= 0 
        positive_bilanz = bilanz[filt]
        percentage = (positive_bilanz.size / len(bilanz.index)) * 100
        
        return percentage
    
    def calc_dunkelflaute(self, bilanz):
        # Create column with boolean values (0 if bilanz < 0 and 1 if bilanz > 0)
        bilanz['Greater_Zero'] = bilanz['Bilanz'].gt(0)
        
        # Remove Datum from index
        bilanz = bilanz.reset_index()
        
        # Check if 'Greater_Zero'-values are consecutive        
        bilanz['Shifted'] = bilanz['Greater_Zero'].shift()
        bilanz['Cumsum'] = (bilanz['Greater_Zero'] != bilanz['Shifted']).cumsum()
        
        # Set and apply filter
        filt = bilanz['Greater_Zero'] == False        
        bilanz = bilanz[filt]
        
        # Group by cumsum column (each cumsum number represents series of consecutive 'Greater_Zero'-values)
        bilanz_grp = bilanz.groupby(['Cumsum'])
        t_dunkelflaute = bilanz_grp.agg({'Datum': ['min', 'max']})
        
        # Add duration of each Dunkelflaute
        t_dunkelflaute['Dauer'] = t_dunkelflaute.iloc[:, 1] - t_dunkelflaute.iloc[:, 0] + timedelta(minutes=15)
        
        return t_dunkelflaute
    
    def calc_max_dunkelflaute(self, bilanz):
        dunkelflaute = self.calc_dunkelflaute(bilanz)
        max_dunkelflaute = dunkelflaute.loc[dunkelflaute['Dauer'].idxmax()]
        
        return max_dunkelflaute
        
    def plot_bilanz(self, location):
        data_to_plot = self.calc_bilanz(location)
        
        # Erstellen der x- und y-Arrays zum plotten
        x = mdates.date2num(data_to_plot.index) # Konvertiert das Datum in ein float (matplotlib kann nur mit floats arbeiten)
        y = data_to_plot['Bilanz'].to_numpy()
        
        # Erstellen des Plots (LineCollection); siehe: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
        fig, ax = plt.subplots()
        
        cols = sns.color_palette("coolwarm", 2)
        
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
        
        return fig    
    
    def plot_bilanz_ee(self, location):
        data_to_plot = self.calc_bilanz_ee(location)
        
        # Erstellen der x- und y-Arrays zum plotten
        x = mdates.date2num(data_to_plot.index) # Konvertiert das Datum in ein float (matplotlib kann nur mit floats arbeiten)
        y = data_to_plot['Bilanz'].to_numpy()
        
        # Erstellen des Plots (LineCollection); siehe: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
        fig, ax = plt.subplots()
        
        cols = sns.color_palette("coolwarm", 2)
        
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
        
        return fig    

class Globalstrahlung(Plot):
    def __init__(self, year, function):
        self.connect_to_sql()
        
        raw_data = pd.read_sql_query('SELECT * FROM Globalstrahlung', self.conn, index_col='Datum')
        raw_data.index = pd.to_datetime(raw_data.index, format='%Y%m%d%H%M')
        raw_data.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
    
        # 10min-Daten in 15min-Daten umwandeln
        raw_data = raw_data.resample('15min').mean()
        
        self.data = self.norm_data(raw_data, function)
        
        today = datetime.now()
        self.data = self.data.apply(lambda row: row*pow(1.022, year - int(today.strftime('%Y'))))
        
        self.disconnect_from_sql()
        
    # Funktioniert noch nicht!
    def plot_globalstrahlung(self):
        #data_to_plot = self.data
        
        #plt.style.use('seaborn')
        #cols = sns.color_palette("Spectral", 4)
        
        #fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
        #plt.plot_date(self.data.index, self.data['SPO'])
        
        #ax.legend(loc='upper left', frameon=1)
        
        # hfmt = mdates.DateFormatter('%b')
        # ax.xaxis.set_major_formatter(hfmt)
        # ax.xaxis.set_major_locator(mdates.MonthLocator())
        
        #ax.set_xlabel('')
        
        #ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        #plt.show()
        
        #return fig
        pass
    
    # Rechnet Durchschnitts-/ Max-/ Min-Wert aus den 3 Jahren aus
    def norm_data(self, data, function):
        data_cpy = data.copy()
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2020
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M")) 
        
        # DataFrame gruppieren nach 'Datum_Normiert'
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        
        # Durchschnitt berechnen
        if function == 'mean':
            new_data = year_grp.mean()
        elif function == 'max':
            new_data = year_grp.max()
        elif function == 'min':
            new_data == year_grp.min()
        
        # 'Datum_Normiert'-Spalte umbennen:
        new_data.index.rename('Datum', inplace=True)
        
        return new_data
        
class Wind(Plot):
    def __init__(self, function):
        self.connect_to_sql()
    
        raw_data = pd.read_sql_query('SELECT * FROM Windgeschwindigkeiten', self.conn, index_col='Datum')
        raw_data.index = pd.to_datetime(raw_data.index, format='%Y%m%d%H%M')
        raw_data.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte

        # 10min-Daten in 15min-Daten umwandeln
        raw_data = raw_data.resample('15min').mean()
        
        self.data = self.norm_data(raw_data, function)
        
        self.disconnect_from_sql()
    
    # Rechnet Durchschnitts-/ Max-/ Min-Wert aus den 3 Jahren aus
    def norm_data(self, data, function):
        data_cpy = data.copy()
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2020
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M")) 
        
        # DataFrame gruppieren nach 'Datum_Normiert'
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        
        # Durchschnitt berechnen
        if function == 'mean':
            new_data = year_grp.mean()
        elif function == 'max':
            new_data = year_grp.max()
        elif function == 'min':
            new_data = year_grp.min()
        
        # 'Datum_Normiert'-Spalte umbennen:
        new_data.index.rename('Datum', inplace=True)
        
        return new_data
    
    # Funktioniert noch nicht!
    def plot_wind(self):
        pass
        

# plot1 = Strommix()
# plot1.plot_strommix('SH')
# plot1.plot_bilanz_ee('Both')
# plot1.plot_bilanz('HH')

# hh_bilanz = plot1.calc_bilanz('HH')
# hh_bilanz_ee = plot1.calc_bilanz_ee('HH')

# sh_bilanz = plot1.calc_bilanz('SH')
# sh_bilanz_ee = plot1.calc_bilanz_ee('SH')

# both_bilanz = plot1.calc_bilanz('Both')
# both_bilanz_ee = plot1.calc_bilanz_ee('Both')

# print('HH alle Energieträger: ' + plot1.calc_pct_positive_bilanz(hh_bilanz).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(hh_bilanz).loc['Dauer'].astype('str'))
# print('HH nur Erneuerbare: ' + plot1.calc_pct_positive_bilanz(hh_bilanz_ee).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(hh_bilanz_ee).loc['Dauer'].astype('str'))

# print('SH alle Energieträger: ' + plot1.calc_pct_positive_bilanz(sh_bilanz).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(sh_bilanz).loc['Dauer'].astype('str'))
# print('SH nur Erneuerbare: ' + plot1.calc_pct_positive_bilanz(sh_bilanz_ee).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(sh_bilanz_ee).loc['Dauer'].astype('str'))

# print('HH + SH alle Energieträger: ' + plot1.calc_pct_positive_bilanz(both_bilanz).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(both_bilanz).loc['Dauer'].astype('str'))
# print('HH + SH nur Erneuerbare: ' + plot1.calc_pct_positive_bilanz(both_bilanz_ee).astype('str'))
# print('Längste Dunkelflaute: ' + plot1.calc_max_dunkelflaute(both_bilanz_ee).loc['Dauer'].astype('str'))


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
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2020 (da 2020 = Schaltjahr)
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
        data = self.calc_mean(self.get_data('Globalstrahlung'))
        
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
        fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
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