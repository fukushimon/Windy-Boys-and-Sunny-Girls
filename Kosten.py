import tkinter as tk

import Energiebilanz
import Home
import Wind
from konstante import style

class Kosten(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(1, weight=1)

#Obere bereich
        label1 = tk.Label(self, text='Szenariosimulation-Kosten', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, columnspan=3, sticky="ew",)

#Mittlere bereich
        self.buttonframe = tk.Frame(self)
        self.buttonframe.config(bg='yellow')
        self.buttonframe.grid(row=1, column=0, sticky='nsew')
        Energiebilanz.Energiebilanz.button_simulation(self)


        textframe = tk.Frame(self)
        textframe.config(bg='red')
        textframe.grid(row=1, column=1, sticky='nsew')
        textframe.grid_columnconfigure(0, weight=1)
        text = tk.Label(textframe, text='Die direkten Kosten der Energiewende – bestehend aus den sog. EEG-Differenzkosten und den\n'
                                        ' KWK-Zuschüssen – beliefen sich in dem Zeitraum 2000-2015 auf ca. 133 Milliarden Euro.\n'
                                        ' Davon entfielen fast 125 iarden Euro auf die EEG-Differenzkosten. Bis 2025 werden die direkten\n'
                                        ' Kosten schätzungsweise auf 425 Milliarden Euro steigen, wobei das Gros davon – fast 283 Milliarden Euro\n'
                                        ' – wieder durch die EEGUmlage generiert wird. Bei den indirekten Kosten der Energiewende sind zunächst \n'
                                        'die Kosten des Übertragungs- und Verteilungsnetzausbaus zu nennen. Diese belaufen sich in dem gesamten \n'
                                        'Zeitraum bis 2025 auf rund 56 Milliarden Euro.')
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
