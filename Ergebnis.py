import tkinter as tk

import Home
import Wind
import Energiebilanz
from konstante import style

class Ergebnis(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(1, weight=1)

#Obere bereich
        label1 = tk.Label(self, text='Szenariosimulation-Ergebnis', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, columnspan=3, sticky="ew",)

#Mittlere bereich
        self.buttonframe = tk.Frame(self)
        self.buttonframe.config(bg='yellow')
        self.buttonframe.grid(row=1, column=0, sticky='nsew')
        Energiebilanz.Energiebilanz.button_simulation(self)


        textframe = tk.Frame(self)
        textframe.config(bg='red')
        textframe.grid(row=1, column=1, columnspan=2, sticky='nsew')
        textframe.grid_columnconfigure(0, weight=1)
        text1 = tk.Label(textframe, text='Wie hoch der Bedarf genau sein wird, hängt unter anderem davon ab,\n'
                                 ' ob direktelektrische Optionen oder synthetische Energieträger stärker\n'
                                 ' im Fokus stehen. Derzeit sollte insbesondere die Entwicklung bei Onshore-Wind\n'
                                 ' zum Beispiel durch eine Erhöhung der Ausschreibungsmengen, der Ausweisung von\n'
                                 ' mehr Flächen und einer Verbesserung des Genehmigungsprozesses beschleunigt werden.')
        text1.config(font=style.FONTTITEL)
        text1.grid(row=0, column=0, padx=5, pady=3, sticky='nsew')

        text2 = tk.Label(textframe, text='Wie hoch der Bedarf genau sein wird, hängt unter anderem davon ab,\n'
                                 ' ob direktelektrische Optionen oder synthetische Energieträger stärker\n'
                                 ' im Fokus stehen. Derzeit sollte insbesondere die Entwicklung bei Onshore-Wind\n'
                                 ' zum Beispiel durch eine Erhöhung der Ausschreibungsmengen, der Ausweisung von\n'
                                 ' mehr Flächen und einer Verbesserung des Genehmigungsprozesses beschleunigt werden.')
        text2.config(font=style.FONTTITEL)
        text2.grid(row=1, column=0, padx=5, pady=3, sticky='nsew')



#Untere bereich
        frame = tk.Frame(self)
        frame.config(background='blue')#style.BACKGROUND)
        frame.grid(row=2, column=0, columnspan=3, sticky='ew')
        frame.grid_columnconfigure(0, weight=2)
        frame.grid_columnconfigure(1, weight=1)

        bto1 = tk.Button(frame, text='Speichern als PDF', **style.STYLE, activebackground=style.BACKGROUND,
                              activeforeground=style.TEXT)
        bto1.grid(row=0, column=2, padx=5, pady=3)
        bto2 = tk.Button(frame, text='Zurück', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Wind.Wind))
        bto2.grid(row=0, column=3, padx=5, pady=3)
        bto3 = tk.Button(frame, text='Schließen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Home.Home))
        bto3.grid(row=0, column=4, padx=5, pady=3)
