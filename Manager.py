import tkinter as tk

from BioGas import BioGas
from Solar import Solar
from Szenarioerstellen import Szenarioerstellen
from Wind import Wind
from konstante import style
from Home import Home
from Szenarioffnen import Szenarioffnen


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Windy boys and Sonny Girls')
        self.config(width="1500", height="800", bg='black')
        self.iconbitmap('Bilder/logo.ico')
        self.minsize(width=1500, height=800)
        self.resizable(width=True, height=True)

# container hinzufügen
        container = tk.Frame(self)
        self.mode = 'Normal'
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.configure(bg=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

# Menubar hinzufügen
        self.Menubar()

# Screens hinzufügen in container
        self.frame = {}
        for F in (Home, Szenarioffnen, Wind, BioGas, Solar):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

# Ausgewhälte screen zeigen
    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()

# Window_Hilfe
    def openHilfe(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Hilfe")
        newWindow.geometry("400x500")
        tk.Label(newWindow, text="This is Hilfe", bg='blue').pack()

# Window_Info
    def openInfo(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Information")
        newWindow.geometry("400x500")
        tk.Label(newWindow, text="This is Info").pack()

# Menu_Bar
    def Menubar(self):
        menu_bar = tk.Menu()
        self.config(menu=menu_bar)
        menu_Datei = tk.Menu(menu_bar, tearoff=False)
        menu_Ansicht = tk.Menu(menu_bar, tearoff=False)

# Menu_Options
        menu_bar.add_cascade(label='Datei', menu=menu_Datei)
        menu_bar.add_cascade(label='Ansicht', menu=menu_Ansicht)
        menu_bar.add_command(label='Hilfe', command=self.openHilfe)
        menu_bar.add_command(label='Über uns', command=self.openInfo)
        menu_bar.add_command(label='Schließen', command=self.destroy)

# Options_items
# Datei
        menu_Datei.add_command(label='Home', command=lambda: self.show_frame(Home))
        menu_Datei.add_command(label='Szenario erstellen', command=lambda: self.show_frame(Solar))
        menu_Datei.add_command(label='Szenario öffnen', command=lambda: self.show_frame(Szenarioffnen))
        menu_Datei.add_separator()
        menu_Datei.add_command(label='Schließen', command=self.destroy)

# Ansicht
        menu_Ansicht.add_command(label='Daten einblenden')
        menu_Ansicht.add_command(label='Karte einblenden')