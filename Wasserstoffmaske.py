import tkinter as tk
from tkinter import *

from konstante import style


class ProduktFrameWasserstoff(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.lbl1 = tk.Label(self, text="Wasserstoff", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(self, text="Wirkungsgrad (P2G2P) ink. Brennstoffzelle: 36 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(self, text="Wirkungsgrad (P2G2P) ink. GuD: 33 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(self, text="Wirkungsgrad Elektroliseur: 74 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(self, text="Wirkungsgrad GuD: 45 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(self, text="Wirkungsgrad Brennstoffzelle: 49 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(self, text="Energiegehalt: 1KgH2 = 33KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)
        lbl8 = tk.Label(self, text="Volumen: 1m^3H2 = 11.89 Kg", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl8.grid(row=1, column=3, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(self, text="Aktuell vorhanden", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)
