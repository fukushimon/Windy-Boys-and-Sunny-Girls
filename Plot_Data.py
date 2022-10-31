import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tkr 
import datetime
from datetime import datetime

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
    c.execute("SELECT Datum, Last, Erzeugung, Importe FROM HH_2021")
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
    
    fig, ax1 = plt.subplots()
    
    ax1.plot_date(dates, values_last, '-', label='Bedarf')
    ax1.plot_date(dates, values_erzeugung, '-', label='Erzeugung')
    
    fig.autofmt_xdate()
    date_format = mdates.DateFormatter('%b %y')
    ax1.xaxis.set_major_formatter(date_format)
    ax1.xaxis.set_major_locator(plt.LinearLocator(12))
    
    ax1.yaxis.set_major_formatter(tkr.FuncFormatter(energy_numfmt))
    ax1.set_ylabel('Stromerzeugung und -verbrauch')
    
    ax1.legend(loc='upper left', frameon=1)
    
    fig.suptitle('Hamburg 2021', fontsize=25)
    fig.set_size_inches(40, 15)
    
    plt.tight_layout()
    plt.show()
    
# custom formatter function: Divides numbers by 1000
def energy_numfmt(x, pos):
    s = '{}'.format(int(x / 1000)) + ' MW'
    return s
    
graph_data_yearly()

c.close()
conn.close()