import pandas as pd
import sqlite3
from datetime import datetime
from Szenario import Szenario
from Plots import Strommix

wind_ausweisflaechen = {
    'Anlagen': ['Gamesa', 'Enercon', 'Gamesa', 'Gamesa', 'Enercon', 'Enercon', 'Enercon', 'Enercon', 'Enercon'],
    'Anzahl': [24, 126, 21, 1, 72, 49, 4, 6, 42],
    'Standorte': ['Leck', 'Schleswig', 'Kiel', 'Kiel', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn']
    }

wind_potenzialflaechen = {
    'Anlagen': ['Gamesa', 'Gamesa', 'Enercon', 'Gamesa', 'Enercon', 'Enercon', 'Enercon', 'Enercon', 'Enercon', 'Enercon', 'Enercon'],
    'Anzahl': [471, 464, 544, 109, 433, 395, 63, 446, 71, 326, 298],
    'Standorte': ['SPO', 'Leck', 'Schleswig', 'Kiel', 'Schleswig', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn', 'Quickborn']
    }

# firstPlot.plot_energy_mix(hh)
# firstPlot.plot_energy_mix(sh)
# firstPlot.plot_energy_mix(total)
    
# scene1 = Szenario('Szenario 1', ['Gamesa', 'Enercon'], [10, 12], ['A', 'C'], ['SunPower'], [200], ['A'])
# scene1.add_to_sql()

# sceneVorrang = Szenario('Szenario Vorranggebiet', ['Gamesa', 'Siemens', 'Enercon'], [10, 12, 5], ['A', 'C', 'D'], ['SunPower', 'LG', 'JA'], [200, 500, 50], ['B', 'C', 'A'])
# sceneVorrang.add_to_sql()

wind_repowering = {
     'Anlagen': ['Enercon', 'Gamesa', 'Gamesa', 'Enercon', 'Gamesa', 'Gamesa', 'Enercon'],
     'Anzahl': [80, 10, 38, 5, 21, 73, 59],
     'Standorte': ['Schleswig', 'Fehmarn', 'Kiel', 'Schleswig', 'SPO', 'Leck', 'Quickborn']
     }
        
solar_potenzialflaechen = {
     'Anlagen': ['SunPower', 'SunPower', 'SunPower'],
     'Flaeche': [125, 243, 80],
     'Standorte': ['Schleswig', 'SPO', 'Leck']
     }

solar_5mrd = {
    'Anlagen': ['SunPower', 'SunPower', 'SunPower'],
    'Flaeche': [13.7, 21.11, 5.28],
    'Standorte': ['Schleswig', 'SPO', 'Leck']
    }

solar_10mrd = {
    'Anlagen': ['SunPower', 'SunPower', 'SunPower'],
    'Flaeche': [2.843, 18.95, 1.895],
    'Standorte': ['Schleswig', 'SPO', 'Leck']
    }

wind_null = {
    'Anlagen': ['Enercon'],
    'Anzahl': [0],
    'Standorte': ['SPO']
    }

solar_null = {
    'Anlagen': ['SunPower'],
    'Flaeche': [0],
    'Standorte': ['Schleswig']
    }

new_scene = Szenario('Szenario 1', 
                     2030, 
                     2021, 
                     2,
                     1,
                     wind_potenzialflaechen['Anlagen'], 
                     wind_potenzialflaechen['Anzahl'],
                     wind_potenzialflaechen['Standorte'], 
                     solar_potenzialflaechen['Anlagen'], 
                     solar_potenzialflaechen['Flaeche'], 
                     solar_potenzialflaechen['Standorte'],
                     1000,
                     1,
                     32,
                     600,
                     10000,
                     1
                     )

new_scene.strommix.plot_speicher('Both')
new_scene.strommix.plot_bilanz_ee('Both')
new_scene.strommix.plot_strommix_ee('Both')
print(new_scene.strommix.calc_pct_positive_bilanz_ee('Both'))

###########################
# scenes = pd.DataFrame(columns=['Name', 'WEA_Anzahl', 'PVA_Flaeche', 'Akku_Anzahl', 'Pumpspeicher_Anzahl', 'Druckluftspeicher_Anzahl', 'Elektrolyseure_Anzahl', 'Deckung', 'Anzahl_Defizite', 'Laengstes_Defizit', 'Kosten'])

# for x in range(0, 2):
#     for y in range(0, 2):
#         # for z in range(0, 10):
#             # Get current time
#             now = datetime.now()
#             # dd/mm/YY H:M:S
#             cur_time = now.strftime("%d/%m/%Y %H:%M")

#             new_scene = Szenario('Szenario {} '.format(x) + cur_time, 
#                                  2030, 
#                                  2021, 
#                                  2,
#                                  1,
#                                  wind_ausweisflaechen['Anlagen'], 
#                                  [num - x for num in wind_ausweisflaechen['Anzahl']],
#                                  wind_ausweisflaechen['Standorte'], 
#                                  solar_potenzialflaechen['Anlagen'], 
#                                  [area - y for area in solar_potenzialflaechen['Flaeche']], 
#                                  solar_potenzialflaechen['Standorte'],
#                                  750000,
#                                  1,
#                                  32,
#                                  130,
                                 
#                                  1
#                                  )
            
#             # new_scene.strommix.plot_speicher('Both')
#             # new_scene.strommix.plot_bilanz_ee('Both')
#             # new_scene.strommix.plot_strommix_ee('Both')
            
#             result = {
#                 'Name': new_scene.name,
#                 'WEA_Anzahl': sum(new_scene.wea_count),
#                 'PVA_Flaeche': sum(new_scene.pv_area),
#                 'Akku_Anzahl': new_scene.num_akku,
#                 'Pumpspeicher_Anzahl': new_scene.num_pump,
#                 'Druckluftspeicher_Anzahl': new_scene.num_druckluft,
#                 'Elektrolyseure_Anzahl': new_scene.num_elektrolyseure,
#                 'Deckung': new_scene.strommix.calc_pct_positive_bilanz_ee('Both'),
#                 'Anzahl_Defizite': len(new_scene.strommix.calc_dunkelflaute_ee('Both').index),
#                 'Laengstes_Defizit': str(new_scene.strommix.calc_max_dunkelflaute_ee('Both')['Dauer']),
#                 'Kosten': new_scene.calc_cost(),
#                 }
            
#             scenes = scenes.append(result, ignore_index=True)
            
#             del new_scene

# conn = sqlite3.connect('Data.db')
# c = conn.cursor()
        
# scenes.to_sql('Simulationen_2030_Ausweisflaechen', conn, if_exists='append')
        
# c.close()
# conn.close()
###########################


# scene_max.strommix.plot_bilanz_ee('Both')
# scene_max.strommix.plot_strommix_ee('Both')
# scene_max.strommix.plot_speicher('Both')
# new_mix = scene_max.strommix.sh_data

# Szenario 'Ausweisflächen + Repowering'
# scene_ausweis = Szenario('Ausweisflaechen', 2030, 1, 
#                       wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'],
#                       solar_potenzialflaechen['Anlagen'], 
#                       solar_potenzialflaechen['Flaeche'], 
#                       solar_potenzialflaechen['Standorte']
#                       )

# scene_ausweis_mix = scene_ausweis.calc_strommix()
# scene_ausweis_mix.plot_bilanz_ee('Both')
# scene_ausweis_mix.plot_strommix_ee('Both')
# print("Szenario Ausweisflächen:")
# print(scene_ausweis_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_ausweis_mix.calc_dunkelflaute_ee('Both'))
# print(scene_ausweis_mix.calc_max_dunkelflaute_ee('Both'))

# Nur Wind
# scene_wind = Szenario('Potenzialflaechen', 2030, 1, 
#                       wind_potenzialflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_potenzialflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_potenzialflaechen['Standorte'] + wind_repowering['Standorte'], 
#                       solar_null['Anlagen'], 
#                       solar_null['Flaeche'], 
#                       solar_null['Standorte']
#                       )

# scene_wind_mix = scene_wind.calc_strommix()
# scene_wind_mix.plot_bilanz_ee('Both')
# scene_wind_mix.plot_strommix_ee('Both')
# print("Szenario Wind:")
# print(scene_wind_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_wind_mix.calc_dunkelflaute_ee('Both'))
# print(scene_wind_mix.calc_max_dunkelflaute_ee('Both'))

# Nur PV
# scene_pv = Szenario('Potenzialflaechen', 2030, 1, 
#                       wind_null['Anlagen'], 
#                       wind_null['Anzahl'], 
#                       wind_null['Standorte'], 
#                       solar_potenzialflaechen['Anlagen'], 
#                       solar_potenzialflaechen['Flaeche'], 
#                       solar_potenzialflaechen['Standorte']
#                       )

# scene_pv_mix = scene_pv.calc_strommix()
# scene_pv_mix.plot_bilanz_ee('Both')
# scene_pv_mix.plot_strommix_ee('Both')
# print("Szenario Solar:")
# print(scene_pv_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_pv_mix.calc_dunkelflaute_ee('Both'))
# print(scene_pv_mix.calc_max_dunkelflaute_ee('Both'))

#Szenario 5Mrd
# scene_5mrd = Szenario('Potenzialflaechen', 2030, 2020, 2, 
#                       wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'], 
#                       solar_5mrd['Anlagen'], 
#                       solar_5mrd['Flaeche'], 
#                       solar_5mrd['Standorte']
#                       )

# scene_5mrd = Szenario('Potenzialflaechen', 2021, 2021, 1, 
#                       wind_ausweisflaechen['Anlagen'], 
#                       wind_ausweisflaechen['Anzahl'], 
#                       wind_ausweisflaechen['Standorte'], 
#                       solar_5mrd['Anlagen'], 
#                       solar_5mrd['Flaeche'], 
#                       solar_5mrd['Standorte']
#                       )



#scene_5mrd_mix = scene_5mrd.calc_strommix()

#scene_5mrd_mix = Strommix(1, 2021)

# bilanz_ee = scene_5mrd_mix.calc_bilanz_ee('Both')
# bilanz_normal = scene_5mrd_mix.calc_bilanz('Both')
# scene_5mrd_mix.plot_bilanz_ee('Both')
# scene_5mrd_mix.plot_strommix('Both')
# print("Szenario 5 Mrd:")
# print(scene_5mrd_mix.calc_pct_positive_bilanz_ee('Both'))
# dunkelflaute = scene_5mrd_mix.calc_dunkelflaute_ee('Both')
# print(dunkelflaute)
# max_dunkelflaute = scene_5mrd_mix.calc_max_dunkelflaute_ee('Both')
# print(max_dunkelflaute)

# filt = ((scene_5mrd_mix.both_data.index >= max_dunkelflaute.iloc[0]) & (scene_5mrd_mix.both_data.index <= max_dunkelflaute.iloc[1]))
# max_dunkel_data_ee = bilanz_ee[filt]
# max_dunkel_data_normal = bilanz_normal[filt]
# max_dunkel_deficit_ee = max_dunkel_data_ee.sum()
# max_dunkel_deficit = max_dunkel_data_normal.sum()


#print(scene_5mrd_mix.both_data.loc[scene_5mrd_mix.both_data['Last'] == scene_5mrd_mix.both_data['Last'].max()])
#new_bilanz = scene_max.calc_speicher(scene_max.strommix)
# mix = scene_max.strommix.both_data
# original_bilanz = scene_max.strommix.calc_bilanz_ee('Both')
# deficits = original_bilanz.loc[original_bilanz['Bilanz'] < 0]

# # Szenario 10Mrd
# scene_10mrd = Szenario('Potenzialflaechen', 2030, 1, 
#                       wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'], 
#                       solar_10mrd['Anlagen'], 
#                       solar_10mrd['Flaeche'], 
#                       solar_10mrd['Standorte']
#                       )

# scene_10mrd_mix = scene_10mrd.calc_strommix()
# scene_10mrd_mix.plot_bilanz_ee('Both')
# scene_10mrd_mix.plot_strommix_ee('Both')
# print("Szenario 10 Mrd:")
# print(scene_10mrd_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_10mrd_mix.calc_dunkelflaute_ee('Both'))
# print(scene_10mrd_mix.calc_max_dunkelflaute_ee('Both'))