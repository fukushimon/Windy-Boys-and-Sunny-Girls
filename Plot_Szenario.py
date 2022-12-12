from Szenario import Szenario

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
    
scene1 = Szenario('Szenario 1', ['Gamesa', 'Enercon'], [10, 12], ['A', 'C'], ['SunPower'], [200], ['A'])
scene1.add_to_sql()

sceneVorrang = Szenario('Szenario Vorranggebiet', ['Gamesa', 'Siemens', 'Enercon'], [10, 12, 5], ['A', 'C', 'D'], ['SunPower', 'LG', 'JA'], [200, 500, 50], ['B', 'C', 'A'])
sceneVorrang.add_to_sql()

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
    'Flaeche': [2.464, 3.79, 0.948],
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

# Szenario 'MAX': Wind- und Solar-Potenzialflächen werden vollständig bebaut (inkl.Repowering)
# scene_max = Szenario('Potenzialflaechen', 2030, 1, 
#                       wind_potenzialflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_potenzialflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_potenzialflaechen['Standorte'] + wind_repowering['Standorte'], 
#                       solar_potenzialflaechen['Anlagen'], 
#                       solar_potenzialflaechen['Flaeche'], 
#                       solar_potenzialflaechen['Standorte']
#                       )

# scene_max_mix = scene_max.calc_strommix()
# scene_max_mix.plot_bilanz_ee('Both')
# scene_max_mix.plot_strommix_ee('Both')
# print("Szenario MAX:")
# print(scene_max_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_max_mix.calc_dunkelflaute_ee('Both'))
# print(scene_max_mix.calc_max_dunkelflaute_ee('Both'))

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

# Szenario 5Mrd
# scene_5mrd = Szenario('Potenzialflaechen', 2030, 1, 
#                       wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
#                       wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
#                       wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'], 
#                       solar_5mrd['Anlagen'], 
#                       solar_5mrd['Flaeche'], 
#                       solar_5mrd['Standorte']
#                       )

# scene_5mrd_mix = scene_5mrd.calc_strommix()
# scene_5mrd_mix.plot_bilanz_ee('Both')
# scene_5mrd_mix.plot_strommix_ee('Both')
# print("Szenario 5 Mrd:")
# print(scene_5mrd_mix.calc_pct_positive_bilanz_ee('Both'))
# print(scene_5mrd_mix.calc_dunkelflaute_ee('Both'))
# print(scene_5mrd_mix.calc_max_dunkelflaute_ee('Both'))

# Szenario 10Mrd
scene_10mrd = Szenario('Potenzialflaechen', 2030, 1, 
                      wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
                      wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
                      wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'], 
                      solar_10mrd['Anlagen'], 
                      solar_10mrd['Flaeche'], 
                      solar_10mrd['Standorte']
                      )

scene_10mrd_mix = scene_10mrd.calc_strommix()
scene_10mrd_mix.plot_bilanz_ee('Both')
scene_10mrd_mix.plot_strommix_ee('Both')
print("Szenario 10 Mrd:")
print(scene_10mrd_mix.calc_pct_positive_bilanz_ee('Both'))
print(scene_10mrd_mix.calc_dunkelflaute_ee('Both'))
print(scene_10mrd_mix.calc_max_dunkelflaute_ee('Both'))


