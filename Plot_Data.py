import pandas as pd
import sqlite3
import matplotlib
matplotlib.use('Agg', force=True)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
import datetime
from datetime import datetime
import seaborn as sns
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

#plt.style.use('seaborn')

conn = sqlite3.connect('Data.db')
c = conn.cursor()

# Daten einlesen aus Datenbank; Gibt ein DataFrame zurück
def get_data(type):
    if type == 'Globalstrahlung':
        df = pd.read_sql_query('SELECT * FROM Globalstrahlung', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format='%Y%m%d%H%M')
        df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte

        # 10min-Daten in 15min-Daten umwandeln
        new_df = df.resample('15min').mean()
        
        return new_df
    
    elif type == 'Windgeschwindigkeiten':
        df = pd.read_sql_query('SELECT * FROM Windgeschwindigkeiten', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format='%Y%m%d%H%M')
        df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte

        # 10min-Daten in 15min-Daten umwandeln
        new_df = df.resample('15min').mean()
        
        return new_df
    
    elif type == 'Strommix_HH':
        df = pd.read_sql_query('SELECT Datum, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kernenergie, Kohle, Erdgas, Speicher, Sonstige_Konventionelle FROM HH', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format="%d.%m.%y %H:%M")
        #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
        return df
    
    elif type == 'Strommix_SH':
        df = pd.read_sql_query('SELECT Datum, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kernenergie, Kohle, Erdgas, Speicher, Sonstige_Konventionelle FROM SH', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")
        #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
        return df
    
    elif type == 'Strombilanz_HH':
        df = pd.read_sql_query('SELECT Datum, Last, Erzeugung FROM HH', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format="%d.%m.%y %H:%M")
        #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
        return df
    
    elif type == 'Strombilanz_SH':
        df = pd.read_sql_query('SELECT Datum, Last, Erzeugung FROM SH', conn, index_col='Datum')
        df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")
        #df.drop('index', axis=1, inplace=True) # Löscht die 'index'-Spalte
        return df
    
    elif type == 'Solarmodule':
        df = pd.read_sql_query('SELECT * FROM Solarmodule', conn)
        return df
    
    elif type == 'WEAs':
        df = pd.read_sql_query('SELECT * FROM WEAs', conn, index_col='Windgeschwindigkeit')
        return df
    else:
        return None

# Ermittelt das Mittel der Daten über mehrere Jahre (z.B. Globalstrahlung, Windgeschwindigkeiten oder Strommix HH)
def calc_mean(data): 
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
def calc_max(data):
    data_cpy = data.copy()
    data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M"))  
    year_grp = data_cpy.groupby(['Datum_Normiert']) 
    max_df = year_grp.max()
    max_df.index.rename('Datum', inplace=True)
    return max_df

# Ermittelt das Mittel der Daten über mehrere Jahre (z.B. Globalstrahlung, Windgeschwindigkeiten oder Strommix HH)
def calc_min(data):
    data_cpy = data.copy()
    data_cpy['Datum_Normiert'] = data_cpy.index.map(lambda x: datetime.strftime(x, "2020-%m-%d %H:%M"))
    year_grp = data_cpy.groupby(['Datum_Normiert'])
    min_df = year_grp.min()
    min_df.index.rename('Datum', inplace=True)
    return min_df

# Berechnet den Gesamt-Stromverbrauch und Stromerzeugung im Jahr x
def calc_total_consumption(year):
    data_HH = calc_mean(get_data('Strombilanz_HH'))
    data_SH = calc_mean(get_data('Strombilanz_SH'))
    
    # Aktueller Gesamtverbrauch in beiden Bundesländern
    data_total = data_HH + data_SH
    #data_total = data_total.to_frame()
    
    # Zukünftiger Gesamtverbrauch mit Faktor 1.02/Jahr
    data_total['Last_Prognose'] = data_total['Last'].apply(lambda row: row*pow(1.02, year-2022))
    
    return data_total

# Berechnet die Globalstrahlung im Jahr x
def calc_total_radiation(year):
    data = calc_mean(get_data('Globalstrahlung'))
    
    # Zukünftige Globalstrahlung mit Faktor 1.022/Jahr
    data_total = data.apply(lambda row: row*pow(1.022, year-2022))
    
    return data_total

# Plottet die Strombilanz
def plot_balance(consumption, production):
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
    
    cmap = ListedColormap(['r', 'b'])
    norm = BoundaryNorm([-1000, 0, 1000], cmap.N)
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(y)
    lc.set_linewidth(1)
    line = ax.add_collection(lc)
    #fig.colorbar(line, ax=ax)
    
    hfmt = mdates.DateFormatter('%b')
    ax.xaxis.set_major_formatter(hfmt)
    ax.xaxis.set_major_locator(mdates.MonthLocator())

    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(-1000, 1000)
    plt.show()
    
    # Wie viel Prozent der Viertelstunden ist gedeckt?
    filt = balance['Bilanz'] >= 0 
    positive_balance = balance[filt] # Liste aller Viertelstunden an denen die Bilanz positiv ist
    
    # In Prozent
    print(positive_balance.size / len(balance.index) * 100)
    
    return balance

# custom formatter function: Energy shall be displayed as MWh
def energy_numfmt(x, pos):
    s = '{}'.format(x.astype(int)) + ' MWh'
    return s

# Plottet den Strommix
def plot_energy_mix(data):
    cols = sns.color_palette("Spectral", 15)
    ax = data.plot.area(color=cols, figsize=(6, 4))
    ax.legend(loc='upper left', frameon=1)
    
    hfmt = mdates.DateFormatter('%b')
    ax.xaxis.set_major_formatter(hfmt)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    ax.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt))
    
    ax.set_xlabel('')
    
    pass


# df = calc_mean(get_data('Strombilanz_HH'))
# hh = plot_balance(df['Last'], df['Erzeugung'])

# df2 = get_data('Strombilanz_SH')
# sh = plot_balance(df2['Last'], df2['Erzeugung'])

# df3 = calc_total_consumption(2022)
# gesamt = plot_balance(df3['Last_Prognose'], df3['Erzeugung'])

# hh = get_data('Strommix_HH').loc['2021']
# sh = get_data('Strommix_SH')
# total = hh + sh

# plot_energy_mix(hh)
# plot_energy_mix(sh)
# plot_energy_mix(total)
    


# Plot Strombilanz
# def plot_strombilanz(data):
#     data_cpy = data.copy()
#     data_cpy.dropna(how='all', subset=['Last'])
#     fig, ax1 = plt.subplots()
#     ax1.plot(data['Last']
#     pass

# def graph_data_daily():
#     c.execute("SELECT Datum, Last, Erzeugung, Importe FROM HH_2021 WHERE Datum < '2021-01-02 00:00:00'")
#     dates = []
#     values_last = []
#     values_erzeugung = []
#     values_importe = []
#     values_energie_total =[]
#     for row in c.fetchall():
#         datetime_obj = pd.to_datetime(row[0])
#         dates.append(datetime_obj)
#         values_last.append(row[1])
#         values_erzeugung.append(row[2])
#         values_importe.append(row[3])
#         values_energie_total.append(row[2] + row[3])
    
#     fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=(True))
    
#     ax1.plot_date(dates, values_last, '-', label='Bedarf')
#     ax1.plot_date(dates, values_erzeugung, '-', label='Erzeugung')
#     ax1.plot_date(dates, values_importe, '-', label='Importe')
    
#     fig.autofmt_xdate()
#     date_format = mdates.DateFormatter('%H:%M')
#     ax1.xaxis.set_major_formatter(date_format)
#     ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
    
#     ax1.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt))
#     ax1.set_ylabel('Stromerzeugung und -verbrauch')
    
#     ax1.legend(loc='upper left')
    
#     ##############
#     ax2.plot_date(dates, values_last, '-', label='Bedarf')
#     ax2.plot_date(dates, values_energie_total, '-', color='darkorange', label='Erzeugung + Importe')
    
#     ax2.xaxis.set_major_formatter(date_format)
#     ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
    
#     ax2.legend(loc='upper left')
    
#     fig.suptitle('Hamburg 01.01.2021', fontsize=25)
    
#     plt.tight_layout()
#     plt.show()
    
# def graph_data_yearly():
#     c.execute("SELECT Datum, Last, Erzeugung, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kohle, Erdgas, Sonstige_Konventionelle FROM HH")
#     dates = []
#     values_last = []
#     values_erzeugung = []
#     values_biomasse = []
#     values_wasser = []
#     values_wind_off = []
#     values_wind_on = []
#     values_pv = []
#     values_sonst_er = []
#     values_kohle = []
#     values_gas = []
#     values_sonst_konv = []
    
#     for row in c.fetchall():
#         datetime_obj = pd.to_datetime(row[0])
#         dates.append(datetime_obj)
#         values_last.append(row[1])
#         values_erzeugung.append(row[2])
#         values_biomasse.append(row[3])
#         values_wasser.append(row[4])
#         values_wind_off.append(row[5])
#         values_wind_on.append(row[6])
#         values_pv.append(row[7])
#         values_sonst_er.append(row[8])
#         values_kohle.append(row[9])
#         values_gas.append(row[10])
#         values_sonst_konv.append(row[11])
    
#     ######################## Plot ########################
    
#     fig1, ax1 = plt.subplots()
#     labels = ['Wasserkraft', 'Biomasse', 'Kohle', 'Erdgas', 'Sonstige Konventionelle', 'Windkraft Onshore', 'Windkraft Offshore', 'Photovoltaik', 'Sonstige Erneuerbare']
    
#     # Colors 
#     cols = sns.color_palette("Spectral", 9)
#     #cols = ["#84c280", "#deb99e", "#c2bc80", "#a6806c", "#a66e6c", "#799eb5", "#5d5cb8", "#f2e15e", "#6ca69a"]
    
#     # Plot Strommix
#     ax1.plot_date(dates, values_last, '-', label='Bedarf', color='tab:gray')
#     #ax1.plot_date(dates, values_erzeugung, '-', label='Erzeugung')
#     ax1.stackplot(dates, values_wasser, values_biomasse, values_kohle, values_gas, values_sonst_konv, values_sonst_er, values_wind_on, values_wind_off, values_pv, labels=labels, colors=cols)
    
#     # Axis formatter
#     fig1.autofmt_xdate() # Make x labels diagonal
#     date_format = mdates.DateFormatter('%b %y') # only show month and year as x tick labels
#     ax1.xaxis.set_major_formatter(date_format)
#     ax1.xaxis.set_major_locator(plt.LinearLocator(12)) # show 12 x tick labels
    
#     ax1.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt)) # y tick labels
    
#     ax1.set_xlim([dates[0], dates[len(dates)-5]])
#     ax1.set_ylabel('Stromerzeugung und -bedarf')
#     ax1.legend(loc='upper left', frameon=1)
#     fig1.suptitle('Hamburg 2021', fontsize=25)
#     fig1.set_size_inches(60, 15)
    
#     # Plot energy balance
#     fig2, ax2 = plt.subplots()
    
#     # Get difference between Erzeugung and Last
#     energy_balance = []
#     for index in range(len(values_erzeugung)):
#         energy_balance.append(values_erzeugung[index] - values_last[index])
        
#     energy_balance_np = np.asarray(energy_balance)
        
#     # Plot different colors by y value
#     supper = np.ma.masked_where(energy_balance_np < 0 , energy_balance_np)
#     slower = np.ma.masked_where(energy_balance_np >= 0, energy_balance_np)  
    
#     ax2.plot(dates, supper, dates, slower)

#     # Plot settings
#     fig2.autofmt_xdate()
#     ax2.xaxis.set_major_formatter(date_format)
#     ax2.xaxis.set_major_locator(plt.LinearLocator(12)) # show 12 x tick labels
    
#     ax2.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt)) # y tick labels
    
#     ax2.set_ylim([-400, 400])
#     ax2.set_xlim([dates[0], dates[len(dates)-5]])
#     ax2.set_ylabel('Strombilanz')
#     fig2.suptitle('Strombilanz Hamburg 2021', fontsize=25)
#     fig2.set_size_inches(60, 15)
    
#     plt.tight_layout()
#     plt.show()
    

    



c.close()
conn.close()