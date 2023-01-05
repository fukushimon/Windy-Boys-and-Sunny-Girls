import tkinter as tk
from tkinter import *
from tkinter import ttk

from konstante import style


class ProduktFrameDruckluft(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.lbl1 = tk.Label(self, text="Druckluftspeicherwerk", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(self, text="Wirkungsgrad: 42%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(self, text="Nennleistung: 321MW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(self, text="Volllestzeit: 5h", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(self, text="Größe der Kavernen: 310.000m^3", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(self, text="Kapazität: 1630 MWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(self, text="Einschaltdauer: 10 min für 100%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)
        lbl8 = tk.Label(self, text="Größe der Anlage: ca. 750m^2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl8.grid(row=1, column=2, padx=5, pady=3, sticky=NSEW)

        lbl9 = tk.Label(self, text="Aktuele Investitionskosten (2022): 120 EUR/KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl9.grid(row=2, column=2, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(self, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)

        self.anzahl = IntVar(self)
        self.anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(self, width=6, from_=0, to=100, textvariable=self.anzahl)
        self.anzahl_spinbox.grid(row=3, column=5)