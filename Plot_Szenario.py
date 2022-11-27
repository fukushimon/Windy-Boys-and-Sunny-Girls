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

from Plot_Ist_Daten import DataPlot
from Szenario import Szenario

# firstPlot = DataPlot()

# hh = firstPlot.get_data_renewables('Strommix_HH').loc['2021']
# sh = firstPlot.get_data_renewables('Strommix_SH')
# total = hh + sh

# firstPlot.plot_energy_mix(hh)
# firstPlot.plot_energy_mix(sh)
# firstPlot.plot_energy_mix(total)
    
scene1 = Szenario('Szenario 1', ['Gamesa', 'Siemens', 'Enercon'], [10, 12, 5], ['A', 'C', 'D'], ['SunPower', 'LG', 'JA'], [200, 500, 50], ['B', 'C', 'A'])
scene1.add_to_sql()


