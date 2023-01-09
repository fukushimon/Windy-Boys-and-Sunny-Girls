import tkinter as tk
from tkinter import *
from tkinter import ttk

from konstante import style


class ProduktFrameSolar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Hersteller
        Hersteller = tk.Label(self, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=25)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)

        self.cbx_hersteller = ttk.Combobox(self, width=50)
        self.cbx_hersteller['values'] = ('', 'Solar-A', 'Solar-B', 'Solar-C', 'Solar-D')
        self.cbx_hersteller.current(0)
        self.cbx_hersteller.grid(row=0, column=1)

        # Standort
        Standort = tk.Label(self, text='Standort', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=25)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        self.cbx_standort = ttk.Combobox(self, width=50)
        self.cbx_standort['values'] = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        self.cbx_standort.current(0)
        self.cbx_standort.grid(row=1, column=1)

        # Modellname
        Modellname = tk.Label(self, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=25)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        self.cbx_modellname = ttk.Combobox(self, width=50)
        self.cbx_modellname['values'] = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        self.cbx_modellname.current(0)
        self.cbx_modellname.grid(row=0, column=3)

        label1 = tk.Label(self, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        label2 = tk.Label(self, text="Fläche", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=25)
        label2.grid(row=0, column=4, padx=5, pady=3)

        # Anzahl
        self.anzahl = IntVar(self)
        self.anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(self, width=10, from_=0, to=100, textvariable=self.anzahl)
        self.anzahl_spinbox.grid(row=0, column=5)

        label2 = tk.Label(self, text="in m^2", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=0, column=6, padx=5, pady=3)

        # Löschen-Button
        self.button_del = tk.Button(self, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                                    activeforeground=style.TEXT, command=self.loeschen)
        self.button_del.grid(row=1, column=5, padx=5, pady=3)
        self.button_clear = tk.Button(self, text='Clear', **style.STYLE, activebackground=style.BACKGROUND,
                                    activeforeground=style.TEXT, command=self.freimachen)
        self.button_clear.grid(row=1, column=6, padx=5, pady=3)

    def loeschen(self):
        self.destroy()

    def freimachen(self):
        self.cbx_hersteller.current(0)
        self.cbx_standort.current(0)
        self.cbx_modellname.current(0)
        var = IntVar(0)
        self.anzahl_spinbox.config(textvariable=var)