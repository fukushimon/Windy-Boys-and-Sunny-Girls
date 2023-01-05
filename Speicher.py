import tkinter as tk
from tkinter import messagebox

import Wind
from Akkumaske import ProduktFrameAkku
from Druckluftspeichermaske import ProduktFrameDruckluft
from Elektrolyseurmaske import ProduktFrameElektrolyseur
from konstante import style
from tkinter import *

from konstante.Product import LIST_SPEICHER, REFERENCE


class Speicher(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        Wind.Wind.button_menu(self)
        # Beschreibung Szenario
        self.szenario_beschreibung()

        label1 = tk.Label(self, text='Scenario Speicher', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        AkkuFrame = ProduktFrameAkku(self)
        AkkuFrame.config(background=style.BACKGROUND)
        AkkuFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(AkkuFrame)

        DruckluftFrame = ProduktFrameDruckluft(self)
        DruckluftFrame.config(background=style.BACKGROUND)
        DruckluftFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(DruckluftFrame)

        elektrolyseurFrame = ProduktFrameElektrolyseur(self)
        elektrolyseurFrame.config(background=style.BACKGROUND)
        elektrolyseurFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(elektrolyseurFrame)

        Wind.Wind.leistung(self)

    def szenario_beschreibung(self):
        datenFrame = tk.Frame(self)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        datenFrame.grid_columnconfigure(1, weight=1)
        datenFrame.grid_columnconfigure(3, weight=1)
        datenFrame.grid_columnconfigure(5, weight=1)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        name = tk.Label(datenFrame, text=REFERENCE[0], **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        name.grid(row=0, column=1, padx=5, pady=3, sticky=NSEW)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        jahr = tk.Label(datenFrame, text=REFERENCE[1], **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        jahr.grid(row=0, column=3, padx=5, pady=3, sticky=NSEW)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        budget = tk.Label(datenFrame, text=REFERENCE[2], **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        budget.grid(row=0, column=5, padx=5, pady=3, sticky=NSEW)

        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def add_produktFrame(self):
        confirm = messagebox.showinfo('Speicher-Art hinzufügen', 'Bitte entschuldigen sie!\n'
                                                                 'Leider sind derzeit keine anderen Speichertypen '
                                                                 'verfügbar. Wir arbeiten daran')
