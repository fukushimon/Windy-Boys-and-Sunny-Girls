import tkinter as tk
import Home
from konstante import style
from tkinter import ttk

class Szenarioerstellen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg='yellow')  # bg=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

# widgets für windFrame

# Widgets in Szenario erstellen
    def init_widgets(self):
# Frame Button
        buttonFrame = tk.Frame(self)
        buttonFrame.config(background=style.BACKGROUND)
        buttonFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        button1 = tk.Button(buttonFrame, text='Wind', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        button1.grid(row=0, column=0, padx=5, pady=3)
        button2 = tk.Button(buttonFrame, text='Solar', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        button2.grid(row=0, column=1, padx=5, pady=3)
        button3 = tk.Button(buttonFrame, text='Biogas', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT)
        button3.grid(row=0, column=2, padx=5, pady=3)

# Frame Wind
        windFrame = tk.Frame(self)
        windFrame.config(background=style.BACKGROUND)
        windFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)
# Wind-Produkte
        produktFrame = tk.Frame(windFrame)
        produktFrame.config(background='blue')#style.BACKGROUND)
        produktFrame.pack(side=tk.TOP,fill=tk.X, expand=True, padx=10, pady=8)#(row=0, column=0)


# widget produktFrame
        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        windFrame.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Simens-Gamesa', 'Nordex')
        windFrame.cbx_Hersteller['values'] = Hersteller
        windFrame.cbx_Hersteller.current(0)
        windFrame.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                           activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        windFrame.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        windFrame.cbx_Standort['values'] = Standort
        windFrame.cbx_Standort.current(0)
        windFrame.cbx_Standort.grid(row=1, column=1)


        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        windFrame.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE', )
        windFrame.cbx_Modellname['values'] = Modellname
        windFrame.cbx_Modellname.current(0)
        windFrame.cbx_Modellname.grid(row=0, column=3)


        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)


        Anzahl = tk.Label(produktFrame, text='Anzahl', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Anzahl.grid(row=0, column=4, padx=5, pady=3)
        windFrame.txt_Anzahl = tk.Entry(produktFrame, width=10)
        windFrame.txt_Anzahl.grid(row=0, column=5)

        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE,activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        button1.grid(row=1, column=5, padx=5, pady=3)

# Solar Frame
        #solarFrame = tk.Frame(self)
        #solarFrame.config(background=style.BACKGROUND)
        #solarFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)
        #biogasFrame = tk.Frame(self)
        #biogasFrame.config(background=style.BACKGROUND)
        #biogasFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)


        tk.Button(self, text='Home', **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                  command=lambda: self.controller.show_frame(Home.Home)).pack(side='bottom', fill=tk.X, padx=10, pady=8)

