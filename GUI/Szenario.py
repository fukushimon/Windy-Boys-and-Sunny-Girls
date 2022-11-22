import tkinter as tk

import Home
from BioGas import BioGas
from Solar import Solar
from Wind import Wind
from konstante import style


class Szenario(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='black')#bg=style.BACKGROUND)
        self.controller = controller
        self.button_menu()

# container hinzufügen
        panel = tk.Frame(self)
        self.mode = 'Normal'
        panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        panel.configure(bg=style.BACKGROUND)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(0, weight=1)

# screens hinzufügen in container
        self.frame = {}
        for F in (Wind, Solar, BioGas):
            frame = F(panel, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.move_frame(Wind)
        self.go_home()

    def move_to_Wind(self):
        self.controller.move_frame(Wind)

    def move_to_Solar(self):
        self.controller.move_frame(Solar)

    def move_to_BioGas(self):
        self.controller.move_frame(BioGas)

# Ausgewhälte screen zeigen
    def move_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()

#Button Frame
    def button_menu(self):
        buttonFrame = tk.Frame(self)
        buttonFrame.config(background=style.BACKGROUND)
        buttonFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        button1 = tk.Button(buttonFrame, text='Wind', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=self.move_to_Wind)
        button1.grid(row=0, column=0, padx=5, pady=3)
        button2 = tk.Button(buttonFrame, text='Solar', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=self.move_to_Solar)
        button2.grid(row=0, column=1, padx=5, pady=3)
        button3 = tk.Button(buttonFrame, text='Biogas', **style.STYLE,
                            activebackground=style.BACKGROUND,activeforeground=style.TEXT, command=self.move_to_BioGas)
        button3.grid(row=0, column=2, padx=5, pady=3)

# Züruck
    def go_home(self):
        tk.Button(self, text='Home', **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                  command=lambda: self.controller.show_frame(Home.Home)).pack(side=tk.TOP, fill=tk.X,
                                                                         padx=10, pady=5)