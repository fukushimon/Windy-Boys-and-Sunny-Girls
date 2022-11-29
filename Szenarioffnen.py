import tkinter as tk

import Home
from konstante import style


class Szenarioffnen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='red')#bg=style.BACKGROUND)
        self.controller = controller

        label1 = tk.Label(self, text='Scenario öffnen', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack()

        tk.Button(self, text='Home', **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                command=lambda: self.controller.show_frame(Home.Home)).pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
