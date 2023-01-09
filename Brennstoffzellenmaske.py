import tkinter as tk
from tkinter import *

from konstante import style


class ProduktFrameBrennstoffzellen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.lbl1 = tk.Label(self, text="Brennstoffzellen", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(self, text="Nennleistung: 1 MW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(self, text="Erzeugte Energie: 8 GWh/a Strom", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(self, text="Investitionskosten 2030: ca. 110 EUR/KW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(self, text="Fläche: 7 m^2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(self, text="Wirkungsgrad: 49 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(self, text="Umwandlung: 1kgH2 -> 16 KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(self, text="Aktuell vorhanden", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)
