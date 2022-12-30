import tkinter as tk
from tkinter import ttk

import Home
import Speicher
import Wind
from konstante import style
from tkinter import *


class Solar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='white')#bg=style.BACKGROUND)
        self.controller = controller
        Wind.Wind.button_menu(self)
        label1 = tk.Label(self, text='Scenario Solar', **style.FONTTITEL,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        self.Solar_frame()
        Wind.Wind.leistung(self)


# Solar Frame
    def Solar_frame(self):
        solarFrame = tk.Frame(self)
        solarFrame.config(background=style.BACKGROUND)
        solarFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

# Scrollbar hinzufügen
        self.canvas = tk.Canvas(solarFrame)
        scrollbar = tk.Scrollbar(solarFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind('<Enter>', self._bind_to_mousewheel)
        self.scrollable_frame.bind('<Leave>', self._unbind_from_mousewheel)


        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

# Beschreibung Szenario
        datenFrame = tk.Frame(self.scrollable_frame)
        datenFrame.config(background='blue')  # style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, expand=True, padx=10, pady=8)  # (row=0, column=0)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        solarFrame.txt_name = tk.Entry(datenFrame, width=50)
        solarFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        solarFrame.txt_jahr = tk.Entry(datenFrame, width=25)
        solarFrame.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        solarFrame.txt_budget = tk.Entry(datenFrame, width=40)
        solarFrame.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

#Solar-Produkte
        self.add_produktFrame()

    def add_produktFrame(self):

        produktFrame = tk.Frame(self.scrollable_frame)
        produktFrame.config(background='blue')  # style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8, expand=True)

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

        label2 = tk.Label(produktFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=0, column=4, padx=5, pady=3)

        anzahl = IntVar(produktFrame)
        anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(produktFrame, width=5, from_=0, to=100, textvariable=anzahl)
        self.anzahl_spinbox.grid(row=0, column=5)

        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=self.loeschen)
        button1.grid(row=1, column=5, padx=5, pady=3)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
    def loeschen(self):
        self.cbx_Hersteller.current(0)
        self.cbx_Standort.current(0)
        self.cbx_Modellname.current(0)
        var = IntVar(0)
        self.anzahl_spinbox.config(textvariable=var)