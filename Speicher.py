import tkinter as tk
from tkinter import messagebox

import Wind
from konstante import style
from tkinter import *


class Speicher(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        self.list_frames = []
        Wind.Wind.button_menu(self)

        label1 = tk.Label(self, text='Scenario Speicher', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        self.speicher_Frame()
        Wind.Wind.leistung(self)

    # Biogas Frame
    def speicher_Frame(self):
        self.speicherFrame = tk.Frame(self)
        self.speicherFrame.config(background=style.BACKGROUND)
        self.speicherFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Beschreibung Szenario
        self.szenario_beschreibung()
        # Akku-Produkte
        akkuFrame = tk.Frame(self.speicherFrame)
        akkuFrame.config(background=style.BACKGROUND)
        akkuFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        akkuFrame.grid_columnconfigure(3, weight=1)
        akkuFrame.grid_columnconfigure(4, weight=1)

        lbl1 = tk.Label(akkuFrame, text="Lithium-Ionen-Batterien", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(akkuFrame, text="Wh-Wirkungsgrad: 95%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(akkuFrame, text="Selbstentladungsrate: <5%/Monat", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(akkuFrame, text="Lade-/Entladezyklen: ca. 10.000", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(akkuFrame, text="Leistung: 5MW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)

        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(akkuFrame, text="Lade-/Entladedauer: 1h", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(akkuFrame, text="Dimensionierung/Kapazität: 5MWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)
        lbl8 = tk.Label(akkuFrame, text="Größe: 50m^2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl8.grid(row=1, column=2, padx=5, pady=3, sticky=NSEW)

        lbl9 = tk.Label(akkuFrame, text="Aktuele Investitionskosten (2022): 500,- EUR", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl9.grid(row=2, column=2, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(akkuFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)

        anzahl = IntVar(akkuFrame)
        anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(akkuFrame, width=6, from_=0, to=100, textvariable=anzahl)
        self.anzahl_spinbox.grid(row=3, column=5)

        # Druckluftspeicher-Produkte
        druckluftspeicherFrame = tk.Frame(self.speicherFrame)
        druckluftspeicherFrame.config(background=style.BACKGROUND)
        druckluftspeicherFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        druckluftspeicherFrame.grid_columnconfigure(3, weight=1)
        druckluftspeicherFrame.grid_columnconfigure(4, weight=1)

        lbl1 = tk.Label(druckluftspeicherFrame, text="Druckluftspeicherwerk", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(druckluftspeicherFrame, text="Wirkungsgrad: 42%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(druckluftspeicherFrame, text="Nennleistung: 321MW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(druckluftspeicherFrame, text="Volllestzeit: 5h", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(druckluftspeicherFrame, text="Größe der Kavernen: 310.000m^3", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(druckluftspeicherFrame, text="Kapazität: 1630 MWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(druckluftspeicherFrame, text="Einschaltdauer: 10 min für 100%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)
        lbl8 = tk.Label(druckluftspeicherFrame, text="Größe der Anlage: ca. 750m^2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl8.grid(row=1, column=2, padx=5, pady=3, sticky=NSEW)

        lbl9 = tk.Label(druckluftspeicherFrame, text="Aktuele Investitionskosten (2022): 120 EUR/KWh", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl9.grid(row=2, column=2, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(druckluftspeicherFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)

        anzahl = IntVar(druckluftspeicherFrame)
        anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(druckluftspeicherFrame, width=6, from_=0, to=100, textvariable=anzahl)
        self.anzahl_spinbox.grid(row=3, column=5)

        # elektrolyseur-Produkte
        elektrolyseurFrame = tk.Frame(self.speicherFrame)
        elektrolyseurFrame.config(background=style.BACKGROUND)
        elektrolyseurFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        elektrolyseurFrame.grid_columnconfigure(3, weight=1)
        elektrolyseurFrame.grid_columnconfigure(4, weight=1)
        elektrolyseurFrame.grid_rowconfigure(1, weight=1)

        lbl1 = tk.Label(elektrolyseurFrame, text="Elektrolyseur von h-Tec systems (PEM)", **style.FONSUBTTITEL,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl1.grid(row=0, column=0, columnspan=6, padx=5, pady=3, sticky=NSEW)

        lbl2 = tk.Label(elektrolyseurFrame, text="Leistung: 2 MW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=NSEW)
        lbl3 = tk.Label(elektrolyseurFrame, text="Nennproduktion: 900 Kg/d bzw. 420 Nm^3/h", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=NSEW)
        lbl4 = tk.Label(elektrolyseurFrame, text="Umwandlung: 43 KWh für 1 KgH2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=NSEW)
        lbl5 = tk.Label(elektrolyseurFrame, text="Fläche: 18,4m^2", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl5.grid(row=1, column=1, padx=5, pady=3, sticky=NSEW)
        lbl6 = tk.Label(elektrolyseurFrame, text="Aktuelle Investitionskosten: 400 EUR/KW", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl6.grid(row=2, column=1, padx=5, pady=3, sticky=NSEW)
        lbl7 = tk.Label(elektrolyseurFrame, text="Wirkungsgrad: 74%", **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl7.grid(row=3, column=1, padx=5, pady=3, sticky=NSEW)

        label2 = tk.Label(elektrolyseurFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=2, column=5, padx=5, pady=3, sticky=NSEW)

        anzahl = IntVar(elektrolyseurFrame)
        anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(elektrolyseurFrame, width=6, from_=0, to=100, textvariable=anzahl)
        self.anzahl_spinbox.grid(row=3, column=5)

    def szenario_beschreibung(self):
        datenFrame = tk.Frame(self.speicherFrame)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        datenFrame.grid_columnconfigure(1, weight=1)
        datenFrame.grid_columnconfigure(3, weight=1)
        datenFrame.grid_columnconfigure(5, weight=1)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        name = tk.Label(datenFrame, text='keine Eingabe', **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        name.grid(row=0, column=1, padx=5, pady=3, sticky=NSEW)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        jahr = tk.Label(datenFrame, text='keine Eingabe ', **style.STYLE,
                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        jahr.grid(row=0, column=3, padx=5, pady=3, sticky=NSEW)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        budget = tk.Label(datenFrame, text='keine Eingabe', **style.STYLE,
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
