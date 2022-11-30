import tkinter as tk
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from PIL import ImageTk, Image
from Wind import Wind
from Szenarioffnen import Szenarioffnen
from konstante import style
from Plot_Ist_Daten import DataPlot


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(background=style.BACKGROUND)
        self.controller = controller

        self.init_widgets()

    def move_to_Wind(self):
        self.controller.show_frame(Wind)

    def move_to_Szenarioffnen(self):
        self.controller.show_frame(Szenarioffnen)

    # Windgets in Home Herstellen
    def init_widgets(self):
        img1 = ImageTk.PhotoImage(Image.open('Bilder/HH.png'))#.resize((950, 380)))
        img2 = ImageTk.PhotoImage(Image.open('Bilder/SH.png'))#.resize((950, 380)))
        img3 = ImageTk.PhotoImage(Image.open('Bilder/HH-SH.png'))#.resize((950, 380)))
        #img_list = [img1, img2, img3]

        # Frame Oberehälfte
        bildFrame = tk.Frame(self)
        bildFrame.config(background=style.BACKGROUND)
        bildFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Bilder
        path = 'Bilder/HH-SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)

        # Frame Unterehälfte
        datenFrame = tk.Frame(self)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=10, pady=8)

        datenFrame.grid_rowconfigure(0, weight=0)
        datenFrame.grid_rowconfigure(1, weight=0)
        datenFrame.grid_rowconfigure(2, weight=0)
        datenFrame.grid_columnconfigure(0, weight=1)
        datenFrame.grid_columnconfigure(1, weight=5)
        datenFrame.grid_columnconfigure(2, weight=1)

        # Alle GridFrame erzeugen
        top_frame = tk.Frame(datenFrame, background=style.BACKGROUND, height=60, pady=3)
        left_frame = tk.Frame(datenFrame, background=style.BACKGROUND, pady=3)
        center_frame = tk.Frame(datenFrame, background=style.BACKGROUND, pady=3)
        bottom_frame = tk.Frame(datenFrame, background=style.BACKGROUND, width=50, height=50, pady=3)

        # Alle gridFrame auf layout sortieren
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        left_frame.grid(row=1, column=0, rowspan=1, sticky="nsew")
        center_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")
        bottom_frame.grid(row=2, column=0, columnspan=3, sticky="ew")

        # Ort Auswahl
        label1 = tk.Label(top_frame, text='Aktuelle Daten', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, padx=5, pady=3)
        button1 = tk.Button(top_frame, text='Hamburg und Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: Home.ImageHH_SH(bildFrame))
        button1.grid(row=0, column=1, padx=5, pady=3)
        button2 = tk.Button(top_frame, text='Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: Home.ImageSH(bildFrame))
        button2.grid(row=0, column=2, padx=5, pady=3)
        button3 = tk.Button(top_frame, text='Hamburg', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: Home.ImageHH(bildFrame))
        button3.grid(row=0, column=3, padx=5, pady=3)

        # Radiobuttons--Jahr Auswählen
        var = tk.IntVar()
        radioButton1 = tk.Radiobutton(left_frame, text='Alle Energietreger', value=1, variable=var, **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT)  # , command=Graph)
        radioButton1.grid(row=0, column=0)
        radioButton2 = tk.Radiobutton(left_frame, text='Nur Erneuerbare', value=2, variable=var, **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT)  # , command=Graph)
        radioButton2.grid(row=1, column=0)

        # Button_Szenarioerstellen
        B1 = tk.Button(left_frame, text='Szenario erstellen', command=self.move_to_Wind,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B1.grid(row=3, column=0, padx=5, pady=3)
        B2 = tk.Button(left_frame, text='Szenario öffnen   ', command=self.move_to_Szenarioffnen,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B2.grid(row=4, column=0, padx=5, pady=3)

        # Graph
        plot1 = DataPlot()
        hh = plot1.get_data_renewables('Strommix_HH').loc['2021']
        canvas = FigureCanvasTkAgg(plot1.plot_energy_mix(hh), center_frame)
        canvas.get_tk_widget().grid(row=0, column=0)
        toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
        toolbar.update()
        canvas._tkcanvas.pack()#grid(row=1, column=0)
        #wenn ich das lesen kann dann funktioniert


    @classmethod
    def ImageSH(cls, bildFrame):
        path = 'Bilder/SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)

    @classmethod
    def ImageHH_SH(cls, bildFrame):
        path = 'Bilder/HH-SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)

    def ImageHH(bildFrame):
        path = 'Bilder/HH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)
