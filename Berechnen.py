import tkinter as tk

import Home
import Solar
import Wind
from konstante import style

class Berechnen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='white')#style.BACKGROUND)
        self.controller = controller


        label1 = tk.Label(self, text='Berechnen', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)


