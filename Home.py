import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import ImageTk, Image
from Wind import Wind
from Szenarioffnen import Szenarioffnen
from konstante import style
from Plots import Strommix
matplotlib.rcParams['backend'] = 'TkAgg'


class Home(tk.Frame):
    #current_plot = 'Both'

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def move_to_wind(self):
        self.controller.show_frame(Wind)

    def move_to_szenarioffnen(self):
        self.controller.show_frame(Szenarioffnen)

    # Windgets in Home Herstellen
    def init_widgets(self):
        # Frame Oberehälfte
        self.bildFrame = tk.Frame(self)
        self.bildFrame.config(background=style.BACKGROUND)
        self.bildFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Bilder
        path = 'Bilder/Both.png'
        img = Image.open(path).resize((1100, 440))
        self.bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(self.bildFrame, image=self.bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)
        bundesland = tk.StringVar()
        bundesland.set('HH-SH')

        # Frame Unterehälfte
        self.datenFrame = tk.Frame(self)
        self.datenFrame.config(background=style.BACKGROUND)
        self.datenFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=10, pady=8)

        self.datenFrame.grid_rowconfigure(0, weight=0)
        self.datenFrame.grid_rowconfigure(1, weight=0)
        self.datenFrame.grid_rowconfigure(2, weight=0)
        self.datenFrame.grid_columnconfigure(0, weight=1)
        self.datenFrame.grid_columnconfigure(1, weight=5)
        self.datenFrame.grid_columnconfigure(2, weight=1)

        # Alle GridFrame erzeugen
        self.top_frame = tk.Frame(self.datenFrame, background=style.BACKGROUND, height=60, pady=3)
        self.left_frame = tk.Frame(self.datenFrame, background=style.BACKGROUND, pady=3)
        self.center_frame = tk.Frame(self.datenFrame, background=style.BACKGROUND, pady=3)
        self.bottom_frame = tk.Frame(self.datenFrame, background=style.BACKGROUND, width=50, height=50, pady=3)

        # Alle gridFrame auf layout sortieren
        self.top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.left_frame.grid(row=1, column=0, rowspan=1, sticky="nsew")
        self.center_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")
        self.bottom_frame.grid(row=2, column=0, columnspan=3, sticky="ew")

        plot_typ = tk.StringVar()
        plot_typ.set('Strommix')
        
        #TOP-FRAME Ort Auswahl
        label1 = tk.Label(self.top_frame, text='Aktuelle Daten', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, padx=5, pady=3)

        button1 = tk.Button(self.top_frame, text='Hamburg und Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: self.show_graph('Both', plot_typ.get()))
        button1.grid(row=0, column=1, padx=5, pady=3)
        button2 = tk.Button(self.top_frame, text='Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: self.show_graph('SH', plot_typ.get()))
        button2.grid(row=0, column=2, padx=5, pady=3)
        button3 = tk.Button(self.top_frame, text='Hamburg', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.show_graph('HH', plot_typ.get()))
        button3.grid(row=0, column=3, padx=5, pady=3)

        # LEFT-FRAME Radiobuttons
        radiobutton1 = tk.Radiobutton(self.left_frame, text='Strommix', variable=plot_typ, value='Strommix',
                                      **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                                      command=lambda: self.show_graph(self.current_plot, plot_typ.get()))
        radiobutton1.grid(row=0, column=0, sticky='W')
        radiobutton2 = tk.Radiobutton(self.left_frame, text='StrommixE', variable=plot_typ, value='StrommixE',
                                      **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                                      command=lambda: self.show_graph(self.current_plot, plot_typ.get()))
        radiobutton2.grid(row=1, column=0, sticky='W')
        radiobutton3 = tk.Radiobutton(self.left_frame, text='Strombilanz', variable=plot_typ, value='Strombilanz',
                                      **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                                      command=lambda: self.show_graph(self.current_plot, plot_typ.get()))
        radiobutton3.grid(row=2, column=0, sticky='W')
        radiobutton4 = tk.Radiobutton(self.left_frame, text='StrombilanzE', variable=plot_typ, value='StrombilanzE',
                                      **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                                      command=lambda: self.show_graph(self.current_plot, plot_typ.get()))
        radiobutton4.grid(row=3, column=0, sticky='W')

        # Button_Szenarioerstellen
        b1 = tk.Button(self.left_frame, text='Szenario erstellen', command=self.move_to_wind,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        b1.grid(row=4, column=0, padx=5, pady=3)
        b2 = tk.Button(self.left_frame, text='Szenario öffnen   ', command=self.move_to_szenarioffnen,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        b2.grid(row=5, column=0, padx=5, pady=3)

        # CENTER-FRAME label und Graph
        # Anzeigen des Plots
        self.toolbar_exists = False
        self.show_graph('Both', plot_typ.get())
        
    def show_graph(self, bundesland, plot_type):
        strommix = Strommix(1, 2022)

        plot = strommix.plot_strommix(bundesland)
        if plot_type == 'Strombilanz':
            plot = strommix.plot_bilanz(bundesland)
        elif plot_type == 'StrombilanzE':
            plot = strommix.plot_bilanz_ee(bundesland)

        elif plot_type == 'StrommixE':
            plot = strommix.plot_strommix_ee(bundesland)

        if self.toolbar_exists:
            self.center_frame.destroy()
            self.bottom_frame = tk.Frame(self.datenFrame, background=style.BACKGROUND, width=50, height=50, pady=3)
            self.center_frame = tk.Frame(self.datenFrame, background='yellow', pady=3)
            self.bottom_frame.grid(row=2, column=0, columnspan=3, sticky="ew")
            self.center_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")
            
        canvas = FigureCanvasTkAgg(plot, self.center_frame)
        canvas.get_tk_widget().grid(row=1, column=0)
        
        toolbar = NavigationToolbar2Tk(canvas, self.bottom_frame)
        toolbar.update()
        
        self.toolbar_exists = True
        self.current_plot = bundesland

        # Change map image
        self.change_map(bundesland)

    def change_map(self, bundesland):
        path = "Bilder/{}.png".format(bundesland)
        img = Image.open(path).resize((1300, 550))
        self.bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(self.bildFrame, image=self.bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)
