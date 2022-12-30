import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
import datetime
from datetime import datetime, timedelta
import seaborn as sns
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


class Plot:
    def __init__(self):
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
    def __init__(self, scene, year):
        super().__init__()
        self.connect_to_sql()
        
        self.scene = scene
        self.year = year
        
        # Hamburg Data
        self.hh_data = pd.read_sql_query('SELECT * FROM HH', self.conn, index_col='Datum')
        self.hh_data.drop('index', axis=1, inplace=True)
        self.hh_data.index = pd.to_datetime(self.hh_data.index, format="%d.%m.%Y %H:%M")
        
        # Schleswig Holstein Data
        self.sh_data = pd.read_sql_query('SELECT * FROM SH', self.conn, index_col='Datum')
        self.sh_data.drop('index', axis=1, inplace=True)
        self.sh_data.index = pd.to_datetime(self.sh_data.index, format="%d.%m.%Y %H:%M")
        
        
        # Current year = 2021
        if scene == 2:
            self.hh_data['Last'] = self.hh_data['Last'] * pow(1.03, self.year - 2021)
            self.sh_data['Last'] = self.sh_data['Last'] * pow(1.03, self.year - 2021)
        elif scene == 3:
            self.hh_data['Last'] = self.hh_data['Last'] * pow(1.06, self.year - 2021)
            self.sh_data['Last'] = self.sh_data['Last'] * pow(1.06, self.year - 2021)
            
        # Sum of both
        self.both_data = self.hh_data + self.sh_data
        
        self.disconnect_from_sql()
    
    def plot_strommix(self, location):
        if location == 'HH':
            data_to_plot = self.hh_data.loc['2021'].copy()
        elif location == 'SH':
            data_to_plot = self.sh_data.loc['2021'].copy()
        elif location == 'Both':
            data_to_plot = self.both_data.loc['2021'].copy()
        else:
            print('No data found!')
            return None
        
        columns_drop = ['Erzeugung']
        if 'Pumpspeicher_Ladestand' in data_to_plot.columns:
            columns_drop.append('Pumpspeicher_Ladestand')
        if 'Akku_Ladestand' in data_to_plot.columns:
            columns_drop.append('Akku_Ladestand')
        if 'Druckluftspeicher_Ladestand' in data_to_plot.columns:
            columns_drop.append('Druckluftspeicher_Ladestand')
            
        data_to_plot.drop(columns_drop, axis=1, inplace=True)
        
        plt.style.use('seaborn')
        cols = sns.color_palette("Spectral", 11)
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 4))
        
        ax.stackplot(data_to_plot.index, (data_to_plot.reset_index(drop=True)).drop('Last', axis=1).T, colors=cols, labels=list(data_to_plot.columns)[1:])
        #ax.plot(data_to_plot.index, data_to_plot['Last'], label='Last', alpha=0.6, color='crimson', linewidth=1)
        
        ax.legend(loc='upper left', frameon=1, bbox_to_anchor=(1.01, 1.015))
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())

        plt.tight_layout()
        
        return fig
    
    def plot_strommix_ee(self, location):
        if location == 'HH':
            data_to_plot = self.hh_data.loc['2021'].copy()
        elif location == 'SH':
            data_to_plot = self.sh_data.loc['2021'].copy()
        elif location == 'Both':
            data_to_plot = self.both_data.loc['2021'].copy()
        else:
            print('No data found!')
            return None
        
        columns_drop = ['Erzeugung', 'Kernenergie', 'Kohle', 'Erdgas', 'Sonstige_Konventionelle']
        if 'Pumpspeicher_Ladestand' in data_to_plot.columns:
            columns_drop.append('Pumpspeicher_Ladestand')
        if 'Akku_Ladestand' in data_to_plot.columns:
            columns_drop.append('Akku_Ladestand')
        if 'Druckluftspeicher_Ladestand' in data_to_plot.columns:
            columns_drop.append('Druckluftspeicher_Ladestand')
            
        data_to_plot.drop(columns_drop, axis=1, inplace=True)
            
        plt.style.use('seaborn')
        cols = sns.color_palette("Spectral", 12)
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 4))
        
        ax.stackplot(data_to_plot.index, (data_to_plot.reset_index(drop=True)).drop('Last', axis=1).T, colors=cols, labels=list(data_to_plot.columns)[1:])
        #ax.plot(data_to_plot.index, data_to_plot['Akku'])
        ax.plot(data_to_plot.index, data_to_plot['Last'], label='Last', alpha=0.9, color='dimgray', linewidth=1)
        
        ax.legend(loc='upper left', frameon=1, bbox_to_anchor=(1.01, 1.015))
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        return fig   
    
    def plot_speicher(self, location):
        
        if location == 'HH':
            data_to_plot = self.hh_data.loc['2021'].copy()
        elif location == 'SH':
            data_to_plot = self.sh_data.loc['2021'].copy()
        elif location == 'Both':
            data_to_plot = self.both_data.loc['2021'].copy()
        else:
            print('No data found!')
            return None
        
        if 'Pumpspeicher_Ladestand' or 'Akku_Ladestand' or 'Druckluftspeicher_Ladestand' in data_to_plot:
            data_to_plot.drop(['Last', 'Erzeugung', 'Biomasse', 'Wasserkraft', 'Wind_Offshore', 'Wind_Onshore', 'Photovoltaik', 'Sonstige_Erneuerbare', 'Kernenergie', 'Kohle', 'Erdgas', 'Sonstige_Konventionelle', 'Speicher'], axis=1, inplace=True)
            
            fig, ax = plt.subplots(1, 1, figsize=(14, 4))
            ax.plot(data_to_plot)
            
            ax.legend(loc='upper left', frameon=1, bbox_to_anchor=(1.01, 1.015), labels=data_to_plot.columns)
            
            locator = mdates.AutoDateLocator()
            formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
            ax.xaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(locator)
            ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        else:
            print('Keine Speicher vorhanden!')
    
    def calc_erzeugung(self, location):
        list_of_erzeuger = ['Biomasse', 'Wasserkraft', 'Wind_Offshore', 'Wind_Onshore', 'Photovoltaik', 'Sonstige_Erneuerbare', 'Kernenergie', 'Kohle', 'Erdgas', 'Sonstige_Konventionelle', 'Speicher']
        if location == 'HH':
            erzeugung = self.hh_data[list_of_erzeuger].sum(axis=1)
        elif location == 'SH':
            erzeugung = self.sh_data[list_of_erzeuger].sum(axis=1)
        elif location == 'Both':
            erzeugung = self.both_data[list_of_erzeuger].sum(axis=1)
        else:
            print('No data found!')
            return None
        
        return erzeugung
    
    def calc_erzeugung_ee(self, location):
        list_of_ee = ['Biomasse', 'Wasserkraft', 'Wind_Offshore', 'Wind_Onshore', 'Photovoltaik', 'Sonstige_Erneuerbare', 'Speicher']
        
        if location == 'HH':
            erzeugung = self.hh_data[list_of_ee].sum(axis=1)
        elif location == 'SH':
            erzeugung = self.sh_data[list_of_ee].sum(axis=1)
        elif location == 'Both':
            erzeugung = self.both_data[list_of_ee].sum(axis=1)
        else:
            print('No data found!')
            return None
        
        return erzeugung
    
    def calc_bilanz(self, location):
        if location == 'HH':
            bilanz = self.calc_erzeugung(location).loc['2021'] - self.hh_data['Last'].loc['2021'] 
        elif location == 'SH':
            bilanz = self.calc_erzeugung(location).loc['2021'] - self.sh_data['Last'].loc['2021']
        elif location == 'Both':
            bilanz = self.calc_erzeugung(location).loc['2021'] - self.both_data['Last'].loc['2021']
        else:
            print('No data found!')
            return None
        
        bilanz = bilanz.to_frame()
        bilanz.rename(columns={0: 'Bilanz'}, inplace=True)
        
        return bilanz.round(3)
    
    def calc_bilanz_ee(self, location):
        if location == 'HH':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.hh_data['Last'].loc['2021'] 
        elif location == 'SH':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.sh_data['Last'].loc['2021'] 
        elif location == 'Both':
            bilanz = self.calc_erzeugung_ee(location).loc['2021'] - self.both_data['Last'].loc['2021']
        else:
            print('No data found!')
            return None
        
        bilanz = bilanz.to_frame()
        bilanz.rename(columns={0: 'Bilanz'}, inplace=True)
        
        return bilanz.round(3)
    
    def calc_pct_positive_bilanz(self, location):
        bilanz = self.calc_bilanz(location)
        filt = bilanz['Bilanz'] >= 0
        positive_bilanz = bilanz[filt]
        percentage = (positive_bilanz.size / len(bilanz.index)) * 100
        
        return percentage
    
    def calc_pct_positive_bilanz_ee(self, location):
        bilanz = self.calc_bilanz_ee(location)
        filt = bilanz['Bilanz'] >= 0
        positive_bilanz = bilanz[filt]
        percentage = (positive_bilanz.size / len(bilanz.index)) * 100
        
        return percentage
    
    def calc_dunkelflaute(self, location):
        bilanz = self.calc_bilanz(location)
        
        # Create column with boolean values (0 if bilanz < 0 and 1 if bilanz > 0)
        bilanz['Greater_Zero'] = bilanz['Bilanz'].ge(0)
        
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
    
    def calc_dunkelflaute_ee(self, location): # Make filter greater equal zero, NOT greater zero!!
        bilanz = self.calc_bilanz_ee(location)
        
        # Create column with boolean values (0 if bilanz < 0 and 1 if bilanz > 0)
        bilanz['Greater_Zero'] = bilanz['Bilanz'].ge(0)
        
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
    
    def calc_max_dunkelflaute(self, location):
        dunkelflaute = self.calc_dunkelflaute(location)
        max_dunkelflaute = dunkelflaute.loc[dunkelflaute['Dauer'].idxmax()]
        
        return max_dunkelflaute
    
    def calc_max_dunkelflaute_ee(self, location):
        dunkelflaute = self.calc_dunkelflaute_ee(location)
        try:
            max_dunkelflaute = dunkelflaute.loc[dunkelflaute['Dauer'].idxmax()]
        except:
            print('Keine Dunkelflauten vorhanden.')
        else:
            return max_dunkelflaute
        
    def plot_bilanz(self, location):
        data_to_plot = self.calc_bilanz(location)
        
        # Erstellen der x- und y-Arrays zum plotten
        x = mdates.date2num(data_to_plot.index) # Konvertiert das Datum in ein float (matplotlib kann nur mit floats arbeiten)
        y = data_to_plot['Bilanz'].to_numpy()
        
        # Erstellen des Plots (LineCollection); siehe: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
        fig, ax = plt.subplots(1, 1, figsize=(14, 4))
        
        plt.style.use('seaborn')
        cols = sns.color_palette("coolwarm", 2)
        
        cmap = ListedColormap([cols[1], cols[0]])
        norm = BoundaryNorm([-10000, 0, 10000], cmap.N)
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(y)
        lc.set_linewidth(1)
        line = ax.add_collection(lc)
        
        ax.set_xlim(x.min(), x.max())
        
        if data_to_plot['Bilanz'].min() == 0:
            min_y = -100
        else:
            min_y = data_to_plot['Bilanz'].min() * 1.1
        
        ax.set_ylim(min_y, data_to_plot['Bilanz'].max() * 1.1)
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        return fig    
    
    def plot_bilanz_ee(self, location):
        data_to_plot = self.calc_bilanz_ee(location)
        
        # Erstellen der x- und y-Arrays zum plotten
        x = mdates.date2num(data_to_plot.index) # Konvertiert das Datum in ein float (matplotlib kann nur mit floats arbeiten)
        y = data_to_plot['Bilanz'].to_numpy()
        
        # Erstellen des Plots (LineCollection); siehe: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
        fig, ax = plt.subplots(1, 1, figsize=(14, 4))
        
        plt.style.use('seaborn')
        cols = sns.color_palette("coolwarm", 2)
        
        cmap = ListedColormap([cols[1], cols[0]])
        norm = BoundaryNorm([-10000, 0, 10000], cmap.N)
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(y)
        lc.set_linewidth(1)
        line = ax.add_collection(lc)
    
        ax.set_xlim(x.min(), x.max())
        
        if data_to_plot['Bilanz'].min() == 0:
            min_y = -100
        else:
            min_y = data_to_plot['Bilanz'].min() * 1.1
        
        ax.set_ylim(min_y, data_to_plot['Bilanz'].max() * 1.1)
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        return fig
    
    def add_to_wind_onshore(self, sh_wind):
        #self.hh_data['Wind_Onshore'] = self.hh_data['Wind_Onshore'] + hh_wind
        self.sh_data['Wind_Onshore'] = self.sh_data['Wind_Onshore'] + sh_wind
        self.both_data['Wind_Onshore'] = self.hh_data['Wind_Onshore'] + self.sh_data['Wind_Onshore']
        
    def add_to_pv(self, sh_pv):
        #self.hh_data['Photovoltaik'] = self.hh_data['Photovoltaik'] + hh_pv
        self.sh_data['Photovoltaik'] = self.sh_data['Photovoltaik'] + sh_pv
        self.both_data['Photovoltaik'] = self.hh_data['Photovoltaik'] + self.sh_data['Photovoltaik']
    
    # Speicher derzeit nur in SH
    def add_speicher(self, speicher, location):
        self.sh_data['Speicher'] = self.sh_data['Speicher'] + speicher['Speicher']
        #self.sh_data.concat(speicher.drop('Speicher', axis=1)) 
        self.both_data = self.hh_data.add(self.sh_data, fill_value=0)
        self.both_data = pd.concat([self.both_data, speicher.drop('Speicher', axis=1)], axis=1)
        

class Globalstrahlung(Plot):
    def __init__(self, future_year, current_year):
        super().__init__()
        self.connect_to_sql()
        
        raw_data = pd.read_sql_query('SELECT * FROM Globalstrahlung', self.conn, index_col='Datum')
        raw_data.index = pd.to_datetime(raw_data.index, format='%Y%m%d%H%M')
        raw_data.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
    
        # 10min-Daten in 15min-Daten umwandeln
        raw_data = raw_data.resample('15min').mean()
        
        # Delete Feb 29
        filt = ((raw_data.index >= '2020-02-29') & (raw_data.index < '2020-03-01'))
        raw_data.drop(raw_data.index[filt], inplace=True)
        
        # Get data from year (2020 or 2021)
        self.data = raw_data.loc[('{}').format(current_year)]
        
        # Calculate future radiation
        self.data = self.data.apply(lambda row: row*pow(1.028, future_year - current_year))
        
        self.disconnect_from_sql()
        
    def plot_globalstrahlung(self, location):
        data_to_plot = self.data
        
        plt.style.use('seaborn')
        
        fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
        plt.plot(data_to_plot.index, data_to_plot[('{}').format(location)], linewidth=1)
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        return fig
    
    # Rechnet Durchschnitts-/ Max-/ Min-Wert aus den 3 Jahren aus
    def norm_data(self, data, function):
        data_cpy = data.copy()
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2021
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2021-%m-%d %H:%M"))
        
        # DataFrame gruppieren nach 'Datum_Normiert'
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        
        # Durchschnitt berechnen
        if function == 'mean':
            new_data = year_grp.mean()
        elif function == 'max':
            new_data = year_grp.max()
        elif function == 'min':
            new_data = year_grp.min()
        else:
            return None
        
        # 'Datum_Normiert'-Spalte umbennen:
        new_data.index.rename('Datum', inplace=True)
        
        new_data.index = pd.to_datetime(new_data.index, format="%Y-%m-%d %H:%M")
        
        return new_data
        
class Wind(Plot):
    def __init__(self, year):
        super().__init__()
        self.connect_to_sql()
    
        raw_data = pd.read_sql_query('SELECT * FROM Windgeschwindigkeiten', self.conn, index_col='Datum')
        raw_data.index = pd.to_datetime(raw_data.index, format='%Y%m%d%H%M')
        raw_data.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte

        # 10min-Daten in 15min-Daten umwandeln
        raw_data = raw_data.resample('15min').mean()
        
        # Delete Feb 29
        filt = ((raw_data.index >= '2020-02-29') & (raw_data.index < '2020-03-01'))
        raw_data.drop(raw_data.index[filt], inplace=True)
        
        # Get data from year (2020 or 2021)
        self.data = raw_data.loc[('{}').format(year)]
        
        # Umwandeln der Windgeschwindigkeiten in int (da Windgeschwindigkeiten in WEA-Tabelle auch in int sind)
        self.data[['Hamburg', 'Schleswig', 'Leck', 'Kiel', 'Fehmarn', 'SPO', 'Quickborn']] = self.data[['Hamburg', 'Schleswig', 'Leck', 'Kiel', 'Fehmarn', 'SPO', 'Quickborn']].astype(int)
        
        self.disconnect_from_sql()
    
    # NOT USED: Rechnet Durchschnitts-/ Max-/ Min-Wert aus den 3 Jahren aus
    def norm_data(self, data, function):
        data_cpy = data.copy()
        
        # Neue Spalte 'Datum_Normiert': Das Datum wird normiert auf 2021
        data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2021-%m-%d %H:%M"))
        
        # DataFrame gruppieren nach 'Datum_Normiert'
        year_grp = data_cpy.groupby(['Datum_Normiert'])
        
        # Durchschnitt berechnen
        if function == 'mean':
            new_data = year_grp.mean()
        elif function == 'max':
            new_data = year_grp.max()
        elif function == 'min':
            new_data = year_grp.min()
        else:
            return None
        
        # 'Datum_Normiert'-Spalte umbennen:
        new_data.index.rename('Datum', inplace=True)
        
        new_data.index = pd.to_datetime(new_data.index, format="%Y-%m-%d %H:%M")
        
        return new_data
    
    def plot_wind(self, location):
        data_to_plot = self.data
        
        plt.style.use('seaborn')
        
        fig, ax = plt.subplots(1, 1, figsize=(17, 5))
        
        plt.plot(data_to_plot.index, data_to_plot[('{}').format(location)], linewidth=1)
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator, formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], zero_formats=['', '%b', '%b-%d', '%b-%d %H:%M', '%b-%d %H:%M', ''], show_offset=False)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(self.energy_numfmt))
        
        ax.set_xlabel('')
        
        ax.set_xlim(data_to_plot.index.min(), data_to_plot.index.max())
        
        return fig