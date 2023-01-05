import tkinter as tk
from tkinter import ttk

import Wind
from Solarmaske import ProduktFrameSolar
from konstante import style
from tkinter import *

from konstante.Product import LIST_SOLAR


class Solar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
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
        self.canvas = tk.Canvas(solarFrame, background=style.BACKGROUND)
        scrollbar = tk.Scrollbar(solarFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, background=style.BACKGROUND)

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
        self.szenario_beschreibung()
# Solar-Produkte
        self.add_produktFrame()

# Beschreibung Szenario
    def szenario_beschreibung(self):
        datenFrame = tk.Frame(self.scrollable_frame)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        datenFrame.grid_columnconfigure(1, weight=1)
        datenFrame.grid_columnconfigure(3, weight=1)
        datenFrame.grid_columnconfigure(5, weight=1)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        self.name = tk.Label(datenFrame, text='keine Eingabe', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.name.grid(row=0, column=1, padx=5, pady=3, sticky=NSEW)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        self.jahr = tk.Label(datenFrame, text='keine Eingabe ', **style.STYLE,
                                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.jahr.grid(row=0, column=3, padx=5, pady=3, sticky=NSEW)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        self.budget = tk.Label(datenFrame, text='keine Eingabe', **style.STYLE,
                                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        self.budget.grid(row=0, column=5, padx=5, pady=3, sticky=NSEW)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

    def add_produktFrame(self):

        produktFrame = ProduktFrameSolar(self.scrollable_frame)
        produktFrame.config(background=style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8, expand=True)

        LIST_SOLAR.append(produktFrame)


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")