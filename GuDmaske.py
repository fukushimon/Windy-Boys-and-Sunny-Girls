import tkinter as tk
from tkinter import *

from konstante import style


class ProduktFrameGuD(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.lbl1 = tk.Label(self, text="Gas-und-Dampf-krafwerke", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        self.lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(self, text="Gesamte installierte Leistung: 451 MWel", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(self, text="Gesamte Tagesstromerzeugung: 5703 MWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(self, text="Wirkungsgrad: 45 %", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(self, text="Umwandlung: 1 KWh -> 14.8 KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(self, text="Reaktionszeit: 5 min", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(self, text="Umwandlung: 1kgH2 -> 16 KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=50)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(self, text="Aktuell vorhanden", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT, width=25)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)
