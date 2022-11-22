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

plt.style.use('seaborn-whitegrid')

conn = sqlite3.connect('HH_Data.db')
c = conn.cursor()

def graph_data_daily():
    c.execute("SELECT Datum, Last, Erzeugung, Importe FROM HH_2021 WHERE Datum < '2021-01-02 00:00:00'")
    dates = []
    values_last = []
    values_erzeugung = []
    values_importe = []
    values_energie_total =[]
    for row in c.fetchall():
        datetime_obj = pd.to_datetime(row[0])
        dates.append(datetime_obj)
        values_last.append(row[1])
        values_erzeugung.append(row[2])
        values_importe.append(row[3])
        values_energie_total.append(row[2] + row[3])
    
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=(True))
    
    ax1.plot_date(dates, values_last, '-', label='Bedarf')
    ax1.plot_date(dates, values_erzeugung, '-', label='Erzeugung')
    ax1.plot_date(dates, values_importe, '-', label='Importe')
    
    fig.autofmt_xdate()
    date_format = mdates.DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(date_format)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
    
    ax1.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt))
    ax1.set_ylabel('Stromerzeugung und -verbrauch')
    
    ax1.legend(loc='upper left')
    
    ##############
    ax2.plot_date(dates, values_last, '-', label='Bedarf')
    ax2.plot_date(dates, values_energie_total, '-', color='darkorange', label='Erzeugung + Importe')
    
    ax2.xaxis.set_major_formatter(date_format)
    ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
    
    ax2.legend(loc='upper left')
    
    fig.suptitle('Hamburg 01.01.2021', fontsize=25)
    
    plt.tight_layout()
    plt.show()
    
def graph_data_yearly():
    c.execute("SELECT Datum, Last, Erzeugung, Biomasse, Wasserkraft, Wind_Offshore, Wind_Onshore, Photovoltaik, Sonstige_Erneuerbare, Kohle, Erdgas, Sonstige_Konventionelle FROM HH_2021")
    dates = []
    values_last = []
    values_erzeugung = []
    values_biomasse = []
    values_wasser = []
    values_wind_off = []
    values_wind_on = []
    values_pv = []
    values_sonst_er = []
    values_kohle = []
    values_gas = []
    values_sonst_konv = []
    
    for row in c.fetchall():
        datetime_obj = pd.to_datetime(row[0])
        dates.append(datetime_obj)
        values_last.append(row[1])
        values_erzeugung.append(row[2])
        values_biomasse.append(row[3])
        values_wasser.append(row[4])
        values_wind_off.append(row[5])
        values_wind_on.append(row[6])
        values_pv.append(row[7])
        values_sonst_er.append(row[8])
        values_kohle.append(row[9])
        values_gas.append(row[10])
        values_sonst_konv.append(row[11])
    
    ######################## Plot ########################
    
    fig1, ax1 = plt.subplots()
    labels = ['Wasserkraft', 'Biomasse', 'Kohle', 'Erdgas', 'Sonstige Konventionelle', 'Windkraft Onshore', 'Windkraft Offshore', 'Photovoltaik', 'Sonstige Erneuerbare']
    
    # Colors 
    cols = sns.color_palette("Spectral", 9)
    #cols = ["#84c280", "#deb99e", "#c2bc80", "#a6806c", "#a66e6c", "#799eb5", "#5d5cb8", "#f2e15e", "#6ca69a"]
    
    # Plot Strommix
    ax1.plot_date(dates, values_last, '-', label='Bedarf', color='tab:gray')
    #ax1.plot_date(dates, values_erzeugung, '-', label='Erzeugung')
    ax1.stackplot(dates, values_wasser, values_biomasse, values_kohle, values_gas, values_sonst_konv, values_sonst_er, values_wind_on, values_wind_off, values_pv, labels=labels, colors=cols)
    
    # Axis formatter
    fig1.autofmt_xdate() # Make x labels diagonal
    date_format = mdates.DateFormatter('%b %y') # only show month and year as x tick labels
    ax1.xaxis.set_major_formatter(date_format)
    ax1.xaxis.set_major_locator(plt.LinearLocator(12)) # show 12 x tick labels
    
    ax1.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt)) # y tick labels
    
    ax1.set_xlim([dates[0], dates[len(dates)-5]])
    ax1.set_ylabel('Stromerzeugung und -bedarf')
    ax1.legend(loc='upper left', frameon=1)
    fig1.suptitle('Hamburg 2021', fontsize=25)
    fig1.set_size_inches(60, 15)
    
    # Plot energy balance
    fig2, ax2 = plt.subplots()
    
    # Get difference between Erzeugung and Last
    energy_balance = []
    for index in range(len(values_erzeugung)):
        energy_balance.append(values_erzeugung[index] - values_last[index])
        
    energy_balance_np = np.asarray(energy_balance)
        
    # Plot different colors by y value
    supper = np.ma.masked_where(energy_balance_np < 0 , energy_balance_np)
    slower = np.ma.masked_where(energy_balance_np >= 0, energy_balance_np)  
    
    ax2.plot(dates, supper, dates, slower)

    # Plot settings
    fig2.autofmt_xdate()
    ax2.xaxis.set_major_formatter(date_format)
    ax2.xaxis.set_major_locator(plt.LinearLocator(12)) # show 12 x tick labels
    
    ax2.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt)) # y tick labels
    
    ax2.set_ylim([-400, 400])
    ax2.set_xlim([dates[0], dates[len(dates)-5]])
    ax2.set_ylabel('Strombilanz')
    fig2.suptitle('Strombilanz Hamburg 2021', fontsize=25)
    fig2.set_size_inches(60, 15)
    
    plt.tight_layout()
    plt.show()
    
# custom formatter function: Energy shall be displayed as MWh
def energy_numfmt(x, pos):
    s = '{}'.format(x) + ' MWh'
    return s
    
graph_data_yearly()

c.close()
conn.close()