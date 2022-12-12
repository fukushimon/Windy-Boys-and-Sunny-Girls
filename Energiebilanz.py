import tkinter as tk

import Ergebnis
import Home
import Kosten
import Stabilitaet
import Wind
from konstante import style

class Energiebilanz(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(1, weight=1)

#Obere bereich
        label1 = tk.Label(self, text='Szenariosimulation-Energiebilanz', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, columnspan=3, sticky="ew",)

#Mittlere bereich
        self.buttonframe = tk.Frame(self)
        self.buttonframe.config(bg='yellow')
        self.buttonframe.grid(row=1, column=0, sticky='nsew')
        self.button_simulation()

        textframe = tk.Frame(self)
        textframe.config(bg='red')
        textframe.grid(row=1, column=1, sticky='nsew')
        textframe.grid_columnconfigure(0, weight=1)
        text = tk.Label(textframe, text='Wie hoch der Bedarf genau sein wird, hängt unter anderem davon ab,\n'
                                 ' ob direktelektrische Optionen oder synthetische Energieträger stärker\n'
                                 ' im Fokus stehen. Derzeit sollte insbesondere die Entwicklung bei Onshore-Wind\n'
                                 ' zum Beispiel durch eine Erhöhung der Ausschreibungsmengen, der Ausweisung von\n'
                                 ' mehr Flächen und einer Verbesserung des Genehmigungsprozesses beschleunigt werden.')
        text.config(font=style.FONTTITEL)
        text.grid(row=3, column=0, padx=5, pady=3, sticky='nsew')




        graphframe = tk.Frame(self)
        graphframe.config(bg='white')
        graphframe.grid(row=1, column=2, sticky='nsew')
        lbl1 = tk.Label(graphframe, text='GRAPH / BILD / IRGENDWAS ???', **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        lbl1.grid(row=0, column=0, padx=5, pady=3)

#Untere bereich
        frame = tk.Frame(self)
        frame.config(background='blue')#style.BACKGROUND)
        frame.grid(row=3, column=0, columnspan=3, sticky='ew')
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


    def button_simulation(self):
        bto1 = tk.Button(self.buttonframe, text='Energiebilanz', **style.STYLE, activebackground=style.BACKGROUND,
                              activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Energiebilanz))
        bto1.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        bto2 = tk.Button(self.buttonframe, text='Stabilität', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Stabilitaet.Stabilitaet))
        bto2.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        bto3 = tk.Button(self.buttonframe, text='Kosten', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Kosten.Kosten))
        bto3.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        bto4 = tk.Button(self.buttonframe, text='Ergebnis', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Ergebnis.Ergebnis))
        bto4.grid(row=3, column=0, padx=5, pady=3, sticky='w')
