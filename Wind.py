import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Scrollbar

import BioGas
import Home
import Solar
from konstante import style

class Wind(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='white')  # bg=style.BACKGROUND)
        self.controller = controller
        self.button_menu()
        self.go_home()
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
        button3 = tk.Button(buttonFrame, text='Biogas', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(BioGas.BioGas))
        button3.grid(row=0, column=2, padx=5, pady=3)


# Wind frame
    def wind_frame(self):
        windFrame = tk.Frame(self)
        windFrame.config(background=style.BACKGROUND)
        windFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Scrollbar hinzufügen
        scrollbar = tk.Scrollbar(windFrame)
        canvas = tk.Canvas(windFrame, bg='red', yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Beschreibung Szenario
        datenFrame = tk.Frame(windFrame)
        datenFrame.config(background='blue')  # style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        windFrame.txt_name = tk.Entry(datenFrame, width=50)
        windFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        windFrame.txt_jahr = tk.Entry(datenFrame, width=25)
        windFrame.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        windFrame.txt_budget = tk.Entry(datenFrame, width=40)
        windFrame.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

# Wind-Produkte
# Produkt 1
        produktFrame = tk.Frame(windFrame)
        produktFrame.config(background='blue')  # style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        windFrame.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Siemens-Gamesa', 'Nordex')
        windFrame.cbx_Hersteller['values'] = Hersteller
        windFrame.cbx_Hersteller.current(0)
        windFrame.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                             activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        windFrame.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        windFrame.cbx_Standort['values'] = Standort
        windFrame.cbx_Standort.current(0)
        windFrame.cbx_Standort.grid(row=1, column=1)

        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        windFrame.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        windFrame.cbx_Modellname['values'] = Modellname
        windFrame.cbx_Modellname.current(0)
        windFrame.cbx_Modellname.grid(row=0, column=3)

        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        Anzahl = tk.Label(produktFrame, text='Anzahl', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Anzahl.grid(row=0, column=4, padx=5, pady=3)
        windFrame.txt_Anzahl = tk.Entry(produktFrame, width=10)
        windFrame.txt_Anzahl.grid(row=0, column=5)

        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT)
        button1.grid(row=1, column=5, padx=5, pady=3)





    def leistung(self):
        leistungFrame = tk.Frame(self)
        leistungFrame.config(background=style.BACKGROUND)
        leistungFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        label_Szenarioname = tk.Label(leistungFrame, text='Gesamteleistung: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        self.txt_name = tk.Entry(leistungFrame, width=50)
        self.txt_name.grid(row=0, column=1, padx=5, pady=3)
        label_Szenarioname = tk.Label(leistungFrame, text=' MW', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=2, padx=5, pady=3)

# Züruck
    def go_home(self):
        tk.Button(self, text='Home', **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                  command=lambda: self.controller.show_frame(Home.Home)).pack(side='bottom', fill=tk.X, padx=10, pady=8)