import tkinter as tk
import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from PIL import ImageTk, Image
from Wind import Wind
from Szenarioffnen import Szenarioffnen
from konstante import style

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
        # img1 = ImageTk.PhotoImage(Image.open('Bilder/HH.png'))#.resize((950, 380)))
        # img2 = ImageTk.PhotoImage(Image.open('Bilder/SH.png'))#.resize((950, 380)))
        # img3 = ImageTk.PhotoImage(Image.open('Bilder/HH-SH.png'))#.resize((950, 380)))
        # img_list = [img1, img2, img3]

        # Frame Oberehälfte
        bildFrame = tk.Frame(self)
        bildFrame.config(background=style.BACKGROUND)
        bildFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Bilder
        path = 'Bilder/HH-SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)
        bundesland = tk.StringVar()
        bundesland.set('HH-SH')

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
        center_frame = tk.Frame(datenFrame, background='yellow', pady=3)
        bottom_frame = tk.Frame(datenFrame, background=style.BACKGROUND, width=50, height=50, pady=3)

        # Alle gridFrame auf layout sortieren
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        left_frame.grid(row=1, column=0, rowspan=1, sticky="nsew")
        center_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")
        bottom_frame.grid(row=2, column=0, columnspan=3, sticky="ew")

        # TOP-FRAME Ort Auswahl
        label1 = tk.Label(top_frame, text='Aktuelle Daten', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=0, column=0, padx=5, pady=3)
        bundeslandlabel = tk.Label(top_frame, text=bundesland.get(), **style.STYLE,
                                   activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        bundeslandlabel.grid(row=0, column=4, padx=5, pady=3)

        button1 = tk.Button(top_frame, text='Hamburg und Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,

                            command=lambda: Home.ImageHH_SH(bildFrame, bundeslandlabel, bundesland))
        button1.grid(row=0, column=1, padx=5, pady=3)
        button2 = tk.Button(top_frame, text='Schleswig-Holstein', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: Home.ImageSH(bildFrame, bundeslandlabel, bundesland))
        button2.grid(row=0, column=2, padx=5, pady=3)
        button3 = tk.Button(top_frame, text='Hamburg', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT,
                            command=lambda: Home.ImageHH(bildFrame, bundeslandlabel, bundesland))
        button3.grid(row=0, column=3, padx=5, pady=3)

        # LEFT-FRAME Radiobuttons
        plot_typ = tk.StringVar()
        plot_typ.set('Strommix')
        radioButton1 = tk.Radiobutton(left_frame, text='Strommix', variable=plot_typ, value='Strommix', **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT,
                                      command=lambda: Home.graph_strommix(labelcontroll, plot_typ, bundesland,
                                                                          center_frame, bottom_frame))
        radioButton1.grid(row=0, column=0)
        radioButton2 = tk.Radiobutton(left_frame, text='StrommixE', variable=plot_typ, value='StrommixE', **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT,
                                      command=lambda: Home.graph_StrommixE(labelcontroll, plot_typ, bundesland,
                                                                           center_frame, bottom_frame))
        radioButton2.grid(row=1, column=0)
        radioButton3 = tk.Radiobutton(left_frame, text='Strombilanz', variable=plot_typ, value='Strombilanz',
                                      **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT,
                                      command=lambda: Home.graph_Strombilanz(labelcontroll, plot_typ, bundesland,
                                                                             center_frame, bottom_frame))
        radioButton3.grid(row=2, column=0)
        radioButton4 = tk.Radiobutton(left_frame, text='StrombilanzE', variable=plot_typ, value='StrombilanzE',
                                      **style.STYLE,
                                      activebackground=style.BACKGROUND,
                                      activeforeground=style.TEXT,
                                      command=lambda: Home.graph_StrombilanzE(labelcontroll, plot_typ, bundesland,
                                                                              center_frame, bottom_frame))
        radioButton4.grid(row=3, column=0)

        # Button_Szenarioerstellen
        B1 = tk.Button(left_frame, text='Szenario erstellen', command=self.move_to_Wind,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B1.grid(row=4, column=0, padx=5, pady=3)
        B2 = tk.Button(left_frame, text='Szenario öffnen   ', command=self.move_to_Szenarioffnen,
                       **style.STYLE, activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        B2.grid(row=5, column=0, padx=5, pady=3)

        # CENTER-FRAME label und Graph
        labelcontroll = tk.Label(center_frame, **style.STYLE,
                                 activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        labelcontroll.grid(row=0, column=0, padx=5, pady=3)
        labelcontroll.config(text=plot_typ.get())

        plot = Strommix(1, 2022)
        canvas = FigureCanvasTkAgg(plot.plot_strommix('HH'), center_frame)

        canvas.get_tk_widget().grid(row=1, column=0)
        toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
        toolbar.grid(row=0, column=0)
        toolbar.update()
        canvas._tkcanvas.grid(row=1, column=0)

    @classmethod
    def ImageHH_SH(cls, bildFrame, bundeslandlabel, bundesland):
        bundesland.set('HH-SH')
        bundeslandlabel.config(text=bundesland.get())
        path = 'Bilder/HH-SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)



    @classmethod
    def ImageSH(cls, bildFrame, bundeslandlabel, bundesland):
        bundesland.set('SH')
        bundeslandlabel.config(text=bundesland.get())
        path = 'Bilder/SH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)


    @classmethod
    def ImageHH(cls, bildFrame, bundeslandlabel, bundesland):
        bundesland.set('HH')
        bundeslandlabel.config(text=bundesland.get())
        path = 'Bilder/HH.png'
        img = Image.open(path).resize((1100, 440))
        bildFrame.image = ImageTk.PhotoImage(img)
        tk.Label(bildFrame, image=bildFrame.image).place(x=0, y=0, relwidth=1, relheight=1)

    @classmethod
    def graph_wahl(cls, labelcontroll, var):
        labelcontroll.config(text=var.get())

    @classmethod
    def graph_wahl(cls, labelcontroll, plot_typ, bundesland, center_frame, bottom_frame):
        labelcontroll.config(text=plot_typ.get())

        if plot_typ.get() == 'Strommix' and bundesland.get() == 'HH-SH':
            print('Strommix HH-SH')
        elif plot_typ.get() == 'Strommix' and bundesland.get() == 'HH':
            print('Strommix HH')
        else:
            print('Strommix SH')

    def graph_strommix(labelcontroll, plot_typ, bundesland, center_frame, bottom_frame):

        if plot_typ.get() == 'Strommix' and bundesland.get() == 'HH-SH':
            print('Strommix HH-SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('Both'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        elif plot_typ.get() == 'Strommix' and bundesland.get() == 'HH':
            print('Strommix HH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('HH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        else:
            print('Strommix SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('SH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()

    @classmethod
    def graph_StrommixE(cls, labelcontroll, plot_typ, bundesland, center_frame, bottom_frame):
        if plot_typ.get() == 'StrommixE' and bundesland.get() == 'HH-SH':
            print('StrommixE HH-SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('Both'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        elif plot_typ.get() == 'StrommixE' and bundesland.get() == 'HH':
            print('StrommixE HH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('HH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        else:
            print('StrommixE SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('SH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()

    @classmethod
    def graph_Strombilanz(cls, labelcontroll, plot_typ, bundesland, center_frame, bottom_frame):
        if plot_typ.get() == 'Strombilanz' and bundesland.get() == 'HH-SH':
            print('Strombilanz HH-SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('Both'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        elif plot_typ.get() == 'Strombilanz' and bundesland.get() == 'HH':
            print('Strombilanz HH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('HH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        else:
            print('Strombilanz SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('SH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()

    @classmethod
    def graph_StrombilanzE(cls, labelcontroll, plot_typ, bundesland, center_frame, bottom_frame):

        if plot_typ.get() == 'StrombilanzE' and bundesland.get() == 'HH-SH':
            print('StrombilanzE HH-SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('Both'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        elif plot_typ.get() == 'StrombilanzE' and bundesland.get() == 'HH':
            print('StrombilanzE HH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('HH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
        else:
            print('StrombilanzE SH')
            plot = Strommix(1, 2022)
            canvas = FigureCanvasTkAgg(plot.plot_strommix_ee('SH'), center_frame)
            canvas.get_tk_widget().grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, bottom_frame)
            toolbar.grid(row=0, column=0)
            toolbar.update()
