import tkinter as tk

import Home
import Solar
import Wind
from konstante import style

class Speicher(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        Wind.Wind.button_menu(self)

        label1 = tk.Label(self, text='Scenario Speicher', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        self.speicher_Frame()
        Wind.Wind.leistung(self)

# Biogas Frame
    def speicher_Frame(self):
        speicherFrame = tk.Frame(self)
        speicherFrame.config(background=style.BACKGROUND)
        speicherFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

# Scrollbar hinzufügen
        scrollbar = tk.Scrollbar(speicherFrame)
        canvas = tk.Canvas(speicherFrame, bg=style.BACKGROUND, yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Beschreibung Szenario
        datenFrame = tk.Frame(speicherFrame)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        speicherFrame.txt_name = tk.Entry(datenFrame, width=50)
        speicherFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        speicherFrame.txt_jahr = tk.Entry(datenFrame, width=25)
        speicherFrame.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                                        activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        speicherFrame.txt_budget = tk.Entry(datenFrame, width=40)
        speicherFrame.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

