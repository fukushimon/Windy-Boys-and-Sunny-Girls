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

#sceneVorrang = Szenario('Szenario Vorranggebiet', ['Gamesa', 'Siemens', 'Enercon'], [10, 12, 5], ['A', 'C', 'D'], ['SunPower', 'LG', 'JA'], [200, 500, 50], ['B', 'C', 'A'])
#sceneVorrang.add_to_sql()
# =======
# wind_repowering = {
#     'Anlagen': ['Enercon', 'Gamesa', 'Gamesa', 'Enercon', 'Gamesa', 'Gamesa', 'Enercon'],
#     'Anzahl': [80, 10, 38, 5, 21, 73, 59],
#     'Standorte': ['Schleswig', 'Fehmarn', 'Kiel', 'Schleswig', 'SPO', 'Leck', 'Quickborn']
#     }
        
# solar_potenzialflaechen = {
#     'Anlagen': ['SunPower', 'SunPower', 'SunPower'],
#     'Flaeche': [125, 243, 80],
#     'Standorte': ['Schleswig', 'SPO', 'Leck']
#     }

# # Szenario 'MAX': Wind- und Solar-Potenzialflächen werden vollständig bebaut (inkl.Repowering)
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

# # Szenario 'Ausweisflächen + Repowering'
# # scene_ausweis = Szenario('Ausweisflaechen', 2030, 1, 
# #                       wind_ausweisflaechen['Anlagen'] + wind_repowering['Anlagen'], 
# #                       wind_ausweisflaechen['Anzahl'] + wind_repowering['Anzahl'], 
# #                       wind_ausweisflaechen['Standorte'] + wind_repowering['Standorte'], 
# #                       solar_potenzialflaechen['Anlagen'], 
# #                       solar_potenzialflaechen['Flaeche'], 
# #                       solar_potenzialflaechen['Standorte']
# #                       )

# # scene_ausweis_mix = scene_ausweis.calc_strommix()
# # scene_ausweis_mix.plot_bilanz_ee('Both')
# # print("Szenario Ausweisflächen:")
# # print(scene_ausweis_mix.calc_pct_positive_bilanz_ee('Both'))
# # print(scene_ausweis_mix.calc_dunkelflaute_ee('Both'))
# # print(scene_ausweis_mix.calc_max_dunkelflaute_ee('Both'))

# >>>>>>> 73e0121e48e87720d9b879fd292bf1fbe2bf782d
