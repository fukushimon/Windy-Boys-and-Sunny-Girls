import tkinter as tk
import Home
import Speicher
import Solar
import Wind
from konstante import style
from tkinter import ttk


class Szenarioerstellen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='yellow')  # bg=style.BACKGROUND)
        self.controller = controller
        self.button_menu()
        self.go_home()

# Frame Button
    def button_menu(self):
        buttonFrame = tk.Frame(self)
        buttonFrame.config(background=style.BACKGROUND)
        buttonFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        button1 = tk.Button(buttonFrame, text='Wind', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Wind.Wind))
        button1.grid(row=0, column=0, padx=5, pady=3)
        button2 = tk.Button(buttonFrame, text='Solar', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Solar.Solar))
        button2.grid(row=0, column=1, padx=5, pady=3)
        button3 = tk.Button(buttonFrame, text='Biogas', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT, command=lambda: self.controller.show_frame(BioGas.BioGas))
        button3.grid(row=0, column=2, padx=5, pady=3)



# Züruck
    def go_home(self):
        tk.Button(self, text='Home', **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                  command=lambda: self.controller.show_frame(Home.Home)).pack(side='bottom', fill=tk.X, padx=10, pady=8)