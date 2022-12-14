import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Scrollbar

import Energiebilanz
import Speicher
import Home
import Solar
from konstante import style


class Wind(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='white')  # bg=style.BACKGROUND)
        self.controller = controller
        self.button_menu()
        label1 = tk.Label(self, text='Scenario Wind', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        self.wind_frame()
        self.leistung()

# Frame Button
    def button_menu(self):
        buttonFrame = tk.Frame(self)
        buttonFrame.config(background=style.BACKGROUND)
        buttonFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        button1 = tk.Button(buttonFrame, text='Wind', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Wind))
        button1.grid(row=0, column=0, padx=5, pady=3)
        button2 = tk.Button(buttonFrame, text='Solar', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Solar.Solar))
        button2.grid(row=0, column=1, padx=5, pady=3)
        button3 = tk.Button(buttonFrame, text='Speicher', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Speicher.Speicher))
        button3.grid(row=0, column=2, padx=5, pady=3)


# Wind frame
    def wind_frame(self):
        self.windFrame = tk.Frame(self)
        self.windFrame.config(background=style.BACKGROUND)
        self.windFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Scrollbar hinzufügen
        scrollbar = tk.Scrollbar(self.windFrame)
        canvas = tk.Canvas(self.windFrame, bg='red', yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        add_button = tk.Button(self.windFrame, text='Neue Anlage +', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)#, command=self.add_produktFrame(self.windFrame))
        add_button.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=8)

#Beschreibung Szenario
        datenFrame = tk.Frame(self.windFrame)
        datenFrame.config(background= style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        self.windFrame.txt_name = tk.Entry(datenFrame, width=50)
        self.windFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        self.windFrame.txt_jahr = tk.Entry(datenFrame, width=25)
        self.windFrame.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        self.windFrame.txt_budget = tk.Entry(datenFrame, width=40)
        self.windFrame.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

# Wind-Produkte
# Produkt 1
        self.add_produktFrame(self.windFrame)
        '''
        produktFrame = tk.Frame(windFrame)
        produktFrame.config(background='blue')  # style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        self.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Siemens-Gamesa', 'Nordex')
        self.cbx_Hersteller['values'] = Hersteller
        self.cbx_Hersteller.current(0)
        self.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                             activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        self.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        self.cbx_Standort['values'] = Standort
        self.cbx_Standort.current(0)
        self.cbx_Standort.grid(row=1, column=1)

        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        self.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        self.cbx_Modellname['values'] = Modellname
        self.cbx_Modellname.current(0)
        self.cbx_Modellname.grid(row=0, column=3)

        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        anzahl = tk.Label(produktFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        anzahl.grid(row=0, column=4, padx=5, pady=3)
        self.anzahl_spinbox = tk.Spinbox(produktFrame, width=5, from_=0, to=100)
        self.anzahl_spinbox.grid(row=0, column=5)


        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=self.loeschen)
        button1.grid(row=1, column=5, padx=5, pady=3)
'''




    def leistung(self):
        leistungFrame = tk.Frame(self)
        leistungFrame.config(background=style.BACKGROUND)
        leistungFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)
        leistungFrame.grid_columnconfigure(3, weight=1)
        leistungFrame.grid_columnconfigure(4, weight=1)

        label_Szenarioname = tk.Label(leistungFrame, text='Gesamteleistung: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        leistungFrame.txt_name = tk.Entry(leistungFrame, width=50)
        leistungFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)
        label_Szenarioname = tk.Label(leistungFrame, text=' MW', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=2, padx=5, pady=3)
        berechnen = tk.Button(leistungFrame, text='Berechnen', **style.STYLE, activebackground=style.BACKGROUND,
                              activeforeground=style.TEXT, command=lambda: Wind.neuen_daten(self))#self.neuen_daten()) #self.controller.show_frame(Energiebilanz.Energiebilanz))
        berechnen.grid(row=0, column=5, padx=5, pady=3)
        Speichern = tk.Button(leistungFrame, text='Speichern', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT)
        Speichern.grid(row=0, column=6, padx=5, pady=3)
        schliessen = tk.Button(leistungFrame, text='Schließen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Home.Home))
        schliessen.grid(row=0, column=7, padx=5, pady=3)

    def loeschen(self):
        self.cbx_Hersteller.current(0)
        self.cbx_Standort.current(0)
        self.cbx_Modellname.current(0)
        self.anzahl_spinbox.config(values=0)

    def neuen_daten(self):
        self.controller.show_frame(Energiebilanz.Energiebilanz)

    def add_produktFrame(self, windFrame):
        produktFrame = tk.Frame(windFrame)
        produktFrame.config(background='blue')  # style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        self.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Siemens-Gamesa', 'Nordex')
        self.cbx_Hersteller['values'] = Hersteller
        self.cbx_Hersteller.current(0)
        self.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        self.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        self.cbx_Standort['values'] = Standort
        self.cbx_Standort.current(0)
        self.cbx_Standort.grid(row=1, column=1)

        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        self.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        self.cbx_Modellname['values'] = Modellname
        self.cbx_Modellname.current(0)
        self.cbx_Modellname.grid(row=0, column=3)

        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        anzahl = tk.Label(produktFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        anzahl.grid(row=0, column=4, padx=5, pady=3)
        self.anzahl_spinbox = tk.Spinbox(produktFrame, width=5, from_=0, to=100)
        self.anzahl_spinbox.grid(row=0, column=5)

        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=self.loeschen)
        button1.grid(row=1, column=5, padx=5, pady=3)

