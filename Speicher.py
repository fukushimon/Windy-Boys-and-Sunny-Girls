import tkinter as tk
from tkinter import messagebox

import Solar
import Wind
from Akkumaske import ProduktFrameAkku
from Brennstoffzellenmaske import ProduktFrameBrennstoffzellen
from Druckluftspeichermaske import ProduktFrameDruckluft
from Elektrolyseurmaske import ProduktFrameElektrolyseur
from GuDmaske import ProduktFrameGuD
from Pumpspeicherkraftwerkmaske import ProduktFramePumpspeicherkraftwerk
from Wasserstoffmaske import ProduktFrameWasserstoff
from konstante import style
from tkinter import *

from konstante.Product import LIST_SPEICHER, REFERENCE


class Speicher(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        Wind.Wind.button_menu(self)

        label1 = tk.Label(self, text='Scenario Speicher', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        Solar.Solar.szenario_beschreibung(self)
        self.Speicher_Frame()

    def Speicher_Frame(self):
        speicherFrame = tk.Frame(self)
        speicherFrame.config(background=style.BACKGROUND)
        speicherFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Scrollbar hinzufügen
        self.canvas = tk.Canvas(speicherFrame, background=style.BACKGROUND)
        scrollbar = tk.Scrollbar(speicherFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, background=style.BACKGROUND)

        #self.scrollable_frame.bind(
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind('<Enter>', self._bind_to_mousewheel)
        self.scrollable_frame.bind('<Leave>', self._unbind_from_mousewheel)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor=NW)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        # Beschreibung Szenario
        Wind.Wind.szenario_beschreibung(self)


        AkkuFrame = ProduktFrameAkku(self.scrollable_frame)
        AkkuFrame.config(background=style.BACKGROUND)
        AkkuFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(AkkuFrame)

        DruckluftFrame = ProduktFrameDruckluft(self.scrollable_frame)
        DruckluftFrame.config(background=style.BACKGROUND)
        DruckluftFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(DruckluftFrame)

        elektrolyseurFrame = ProduktFrameElektrolyseur(self.scrollable_frame)
        elektrolyseurFrame.config(background=style.BACKGROUND)
        elektrolyseurFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(elektrolyseurFrame)

        wasserstoffFrame = ProduktFrameWasserstoff(self.scrollable_frame)
        wasserstoffFrame.config(background=style.BACKGROUND)
        wasserstoffFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(wasserstoffFrame)

        pumpspeicherFrame = ProduktFramePumpspeicherkraftwerk(self.scrollable_frame)
        pumpspeicherFrame.config(background=style.BACKGROUND)
        pumpspeicherFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(pumpspeicherFrame)

        brennstoffzellenFrame = ProduktFrameBrennstoffzellen(self.scrollable_frame)
        brennstoffzellenFrame.config(background=style.BACKGROUND)
        brennstoffzellenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(brennstoffzellenFrame)

        gudFrame = ProduktFrameGuD(self.scrollable_frame)
        gudFrame.config(background=style.BACKGROUND)
        gudFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        LIST_SPEICHER.append(gudFrame)

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
