import tkinter as tk

from konstante import style
from Home import Home
from Szenarioerstellen import Szenarioerstellen
from Szenarioffnen import Szenarioffnen

class Manager(tk.Tk):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Windy boys and Sonny Girls')
        self.config(width="1500", height="800", bg='black')
        self.iconbitmap('Bilder/logo.ico')
        self.minsize(width=1500, height=900)
        self.resizable(width=True, height=True)

# container hinzufügen
        container = tk.Frame(self)
        self.mode = 'Normal'
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.configure(bg=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

#Menubar hinzufügen
        self.Menubar()

# screens hinzufügen in container
        self.frame = {}
        for F in (Home, Szenarioerstellen, Szenarioffnen):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

#Ausgewhälte screen zeigen
    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()

# Menu_Bar
    def Menubar(self):
        menu_bar = tk.Menu()
        self.config(menu=menu_bar)
        menu_Datei = tk.Menu(menu_bar, tearoff=False)
        menu_Ansicht = tk.Menu(menu_bar, tearoff=False)
# Menu_Options
        menu_bar.add_cascade(label='Datei', menu=menu_Datei)
        menu_bar.add_cascade(label='Ansicht', menu=menu_Ansicht)
        menu_bar.add_command(label='Hilfe')  # , command=self.openHilfe)
        menu_bar.add_command(label='Info')  # , command=self.openInfo)
        menu_bar.add_command(label='Schließen', command=self.destroy)

# Options_items
# Datei
        menu_Datei.add_command(label='Home')#, command=lambda: app.switch_frame(StartPage))
        menu_Datei.add_command(label='Szenario erstellen')#, command=self.move_to_Szenarioerstellen)
        menu_Datei.add_command(label='Szenario öffnen')#, command=self.move_to_Szenarioffnen)
        menu_Datei.add_separator()
        menu_Datei.add_command(label='Schließen', command=self.destroy)
# Ansicht
        menu_Ansicht.add_command(label='Daten einblenden')
        menu_Ansicht.add_command(label='Karte einblenden')