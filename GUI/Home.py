import tkinter as tk
from PIL import ImageTk, Image

from Szenarioerstellen import Szenarioerstellen
from Szenarioffnen import Szenarioffnen
from konstante import style

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value='Normal')

        self.init_widgets()
        
    def move_to_Szenarioerstellen(self):
        self.controller.show_frame(Szenarioerstellen)

    def move_to_Szenarioffnen(self):
        self.controller.show_frame(Szenarioffnen)

    def ImagenHH(bildFrame):
        path = 'Bilder/HHcopy.png'
        img = Image.open(path)#.resize((900, 350))  # ((300, 150))
        bildFrame.configure(image=img)
        bildFrame.image = img

#Windgets in Home Herstellen
    def init_widgets(self):

#Frame Oberehälfte
        bildFrame = tk.Frame(self)
        bildFrame.config(background=style.BACKGROUND)
        bildFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

#Bilder
        path = 'Bilder/HH-SHcopy.png'
        img = Image.open(path).resize((950, 380))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)

#Frame Unterehälfte
        datenFrame = tk.Frame(self)
        datenFrame.config(bg=style.COMPONENT)
        datenFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)
        label1 = tk.Label(datenFrame, text='Aktuelle Daten', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, padx=5, pady=3)
# Ort Auswahl
        button1 = tk.Button(datenFrame, text='Hamburg und Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT) #, command=lambda: ImagenHH_SH)
        button1.grid(row=0, column=1, padx=5, pady=3)
        button2 = tk.Button(datenFrame, text='Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT) #, command=lambda: ImagenSH)
        button2.grid(row=0, column=2, padx=5, pady=3)
        button3 = tk.Button(datenFrame, text='Hamburg', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: Home.ImagenHH)
        button3.grid(row=0, column=3, padx=5, pady=3)

# Radiobuttons--Jahr Auswählen
        var = tk.IntVar()
        radioButton1 = tk.Radiobutton(datenFrame, text='2020', value=1, variable=var, **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)#, command=Graph)
        radioButton1.grid(row=1, column=0)
        radioButton2 = tk.Radiobutton(datenFrame, text='2021', value=2, variable=var, **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)#, command=Graph)
        radioButton2.grid(row=2, column=0)
        radioButton3 = tk.Radiobutton(datenFrame, text='2022', value=3, variable=var, **style.STYLE,
                                      activebackground=style.BACKGROUND, activeforeground=style.TEXT)#, command=Graph)
        radioButton3.grid(row=3, column=0)

# Platzhalter für Graph
        graph = Image.open('Bilder/graph.png').resize((1100, 300))
        datenFrame.image = ImageTk.PhotoImage(graph)
        label2 = tk.Label(datenFrame, image=datenFrame.image).place(x=150, y=75, width=1100, height=300)
        label3 = tk.Label(datenFrame,text='Bescheibung1',bg='yellow').place(x=1275, y=100, width=175, height=25)
        label4 = tk.Label(datenFrame,text='Bescheibung2',bg='blue').place(x=1275, y=125, width=175, height=25)
        label5 = tk.Label(datenFrame,text='Bescheibung3',bg='orange').place(x=1275, y=150, width=175, height=25)
        label6 = tk.Label(datenFrame,text='Bescheibung4',bg='green').place(x=1275, y=175, width=175, height=25)
        label6 = tk.Label(datenFrame,text='Bescheibung5',bg='red').place(x=1275, y=200, width=175, height=25)
        label6 = tk.Label(datenFrame,text='Bescheibung6',bg='cyan').place(x=1275, y=225, width=175, height=25)

#Button_Szenarioerstellen
        B1 = tk.Button(datenFrame, text='Szenario erstellen', command=self.move_to_Szenarioerstellen,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B1.grid(row=7, column=0, padx=5, pady=3)
        B2 = tk.Button(datenFrame, text='Szenario öffnen   ', command=self.move_to_Szenarioffnen,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B2.grid(row=8, column=0, padx=5, pady=3)

