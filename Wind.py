import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

import Energiebilanz
import ScrollabelFrame
import Speicher
import Home
import Solar
from konstante import style


class Wind(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg=style.BACKGROUND)
        self.controller = controller
        self.button_menu()
        label1 = tk.Label(self, text='Scenario Wind', **style.FONTTITEL,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        self.wind_frame()
        self.leistung()

# Frame Button
    def button_menu(self):
        buttonFrame = tk.Frame(self)
        buttonFrame.config(background=style.BACKGROUND)
        buttonFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        button1 = tk.Button(buttonFrame, text='Wind', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: self.controller.show_frame(Wind))
        button1.grid(row=0, column=0, padx=5, pady=3)
        button2 = tk.Button(buttonFrame, text='Solar', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: self.controller.show_frame(Solar.Solar))
        button2.grid(row=0, column=1, padx=5, pady=3)
        button3 = tk.Button(buttonFrame, text='Speicher', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                            command=lambda: self.controller.show_frame(Speicher.Speicher))
        button3.grid(row=0, column=2, padx=5, pady=3)


# Wind frame
    def wind_frame(self):

        self.windFrame = tk.Frame(self)
        self.windFrame.config(background=style.BACKGROUND)
        self.windFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Scrollbar hinzufügen
        self.canvas = tk.Canvas(self.windFrame)
        scrollbar = ttk.Scrollbar(self.windFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind('<Enter>', self._bind_to_mousewheel)
        self.scrollable_frame.bind('<Leave>', self._unbind_from_mousewheel)


        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

#Beschreibung Szenario
        datenFrame = tk.Frame(self.scrollable_frame)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        self.windFrame.txt_name = tk.Entry(datenFrame, width=50)
        self.windFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        self.windFrame.txt_jahr = tk.Entry(datenFrame, width=25)
        self.windFrame.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        self.windFrame.txt_budget = tk.Entry(datenFrame, width=40)
        self.windFrame.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)

# Wind-Produkte
# Produkt 1
        self.add_produktFrame()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")


    def leistung(self):
        leistungFrame = tk.Frame(self)
        leistungFrame.config(background=style.BACKGROUND)
        leistungFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)  # (row=0, column=0)
        leistungFrame.grid_columnconfigure(3, weight=1)
        leistungFrame.grid_columnconfigure(4, weight=1)
        leistungFrame.grid_columnconfigure(5, weight=1)

        label_Szenarioname = tk.Label(leistungFrame, text='Gesamteleistung: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        leistungFrame.txt_name = tk.Entry(leistungFrame, width=50)
        leistungFrame.txt_name.grid(row=0, column=1, padx=5, pady=3)
        label_Szenarioname = tk.Label(leistungFrame, text=' MW', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=2, padx=5, pady=3)

        anlage_button = tk.Button(leistungFrame, text='Neue Anlage +', **style.STYLE,
                               activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                               command=lambda: self.add_produktFrame())
        anlage_button.grid(row=0, column=4, padx=5, pady=3, sticky=EW)  #pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=8)

        berechnen = tk.Button(leistungFrame, text='Berechnen', **style.STYLE, activebackground=style.BACKGROUND,
                              activeforeground=style.TEXT, command=lambda: Wind.faktoren_berücksichtigen(self))
        berechnen.grid(row=0, column=6, padx=5, pady=3)
        Speichern = tk.Button(leistungFrame, text='Speichern', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT)
        Speichern.grid(row=0, column=7, padx=5, pady=3)
        schliessen = tk.Button(leistungFrame, text='Schließen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Home.Home))
        schliessen.grid(row=0, column=8, padx=5, pady=3)

    def loeschen(self):
        self.cbx_Hersteller.current(0)
        self.cbx_Standort.current(0)
        self.cbx_Modellname.current(0)
        var = IntVar(0)
        self.anzahl_spinbox.config(textvariable=var)

    def berechnen(self):
        confirm = messagebox.askyesnocancel('Berechnung', 'asdfghjklöpoiuztrewqyxcvbnm')
        if confirm:
            self.controller.show_frame(Energiebilanz.Energiebilanz)
            self.newWindow.destroy()
        elif confirm is None:
            self.newWindow.destroy()
            self.faktoren_berücksichtigen()
        else:
            self.newWindow.destroy()



    ########################

    def faktoren_berücksichtigen(self):
        self.newWindow = tk.Toplevel(self)
        self.newWindow.title("Berechnen")
        self.newWindow.geometry("400x500")
        self.newWindow.config(bg=style.BACKGROUND)
        tk.Label(self.newWindow, text="Faktoren zu berücksichtigen ", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=0, columnspan=2, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Wetterdaten: ", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=1, columnspan=1, sticky=W, padx=5, pady=3)
        option1 = IntVar()
        option2 = IntVar()
        Checkbutton(self.newWindow, text="(2020/2021", variable=option1, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=2, column=0, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="2022", variable=option2, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=2, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Globalstrahlungsfaktor", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=3, columnspan=1, sticky=W, padx=5, pady=3)
        option3 = IntVar()
        option4 = IntVar()
        Checkbutton(self.newWindow, text="Ja", variable=option3, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=4, column=0, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="Nein", variable=option4, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=4, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Repowering", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=5, columnspan=1, sticky=W, padx=5, pady=3)
        option5 = IntVar()
        option6 = IntVar()
        Checkbutton(self.newWindow, text="Ja", variable=option5, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=6, column=0, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="Nein", variable=option6, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=6, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Verbaruchsszenarien", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=7, columnspan=1, sticky=W, padx=5, pady=3)
        option7 = IntVar()
        option8 = IntVar()
        option9 = IntVar()
        Checkbutton(self.newWindow, text="Bundesregierung", variable=option7, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=8, column=0, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="alles bleibt gleich", variable=option8, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=8, column=1, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="Sektorenkopplung", variable=option9, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=9, column=0, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="PR-Faktor verändern?", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=10, columnspan=1, sticky=W, padx=5, pady=3)
        option10 = IntVar()
        option11 = IntVar()
        Checkbutton(self.newWindow, text="Ja", variable=option10, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=11, column=0, sticky=W, padx=5, pady=3)
        Checkbutton(self.newWindow, text="Nein", variable=option11, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=11, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Startwert  der Speicher in % : ", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=12, columnspan=1, sticky=W, padx=5, pady=3)

        ladung = IntVar(self.newWindow)
        ladung.set(0)
        self.ladung_spinbox = tk.Spinbox(self.newWindow, width=5, from_=0, to=100, textvariable=ladung)
        self.ladung_spinbox.grid(row=13, sticky=W, padx=5, pady=3)

        weiter_button = tk.Button(self.newWindow, text='Weiter', **style.STYLE,
                               activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                               command=lambda: self.berechnen())
        weiter_button.grid(row=14, column=0, sticky=E, padx=5, pady=3)

        abbrechen_button = tk.Button(self.newWindow, text='Abbrechen', **style.STYLE,
                               activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                               command=lambda: self.newWindow.destroy())
        abbrechen_button.grid(row=14, column=1, sticky=E, padx=5, pady=3)

        ########################

    def add_produktFrame(self):

        produktFrame = tk.Frame(self.scrollable_frame)
        produktFrame.config(background='blue')  # style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8, expand=True)

        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        self.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Siemens-Gamesa', 'Nordex')
        self.cbx_Hersteller['values'] = Hersteller
        self.cbx_Hersteller.current(0)
        self.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        self.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        self.cbx_Standort['values'] = Standort
        self.cbx_Standort.current(0)
        self.cbx_Standort.grid(row=1, column=1)

        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        self.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        self.cbx_Modellname['values'] = Modellname
        self.cbx_Modellname.current(0)
        self.cbx_Modellname.grid(row=0, column=3)

        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        label2 = tk.Label(produktFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label2.grid(row=0, column=4, padx=5, pady=3)

        anzahl = IntVar(produktFrame)
        anzahl.set(0)
        self.anzahl_spinbox = tk.Spinbox(produktFrame, width=5, from_=0, to=100, textvariable=anzahl)
        self.anzahl_spinbox.grid(row=0, column=5)

        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=self.loeschen)
        button1.grid(row=1, column=5, padx=5, pady=3)












        '''
        Hersteller = tk.Label(produktFrame, text='Hersteller', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Hersteller.grid(row=0, column=0, padx=5, pady=3)
        self.cbx_Hersteller = ttk.Combobox(produktFrame, width=50)
        Hersteller = ('', 'Enercon', 'Vestas', 'Siemens-Gamesa', 'Nordex')
        self.cbx_Hersteller['values'] = Hersteller
        self.cbx_Hersteller.current(0)
        self.cbx_Hersteller.grid(row=0, column=1)

        Standort = tk.Label(produktFrame, text='Standort', **style.STYLE,
                            activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Standort.grid(row=1, column=0, padx=5, pady=3)
        self.cbx_Standort = ttk.Combobox(produktFrame, width=50)
        Standort = ('', 'Schleswig-Holstein A', 'Schleswig-Holstein B', 'Schleswig-Holstein C',
                    'Schleswig-Holstein D', 'Schleswig-Holstein E', 'Schleswig-Holstein F', 'Hamburg')
        self.cbx_Standort['values'] = Standort
        self.cbx_Standort.current(0)
        self.cbx_Standort.grid(row=1, column=1)

        Modellname = tk.Label(produktFrame, text='Modellname', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        Modellname.grid(row=0, column=2, padx=5, pady=3)
        self.cbx_Modellname = ttk.Combobox(produktFrame, width=50)
        Modellname = ('', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',)
        self.cbx_Modellname['values'] = Modellname
        self.cbx_Modellname.current(0)
        self.cbx_Modellname.grid(row=0, column=3)

        label1 = tk.Label(produktFrame, text='Wetter daten werden automatisch beruchsichtig', **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label1.grid(row=1, column=3, padx=5, pady=3)

        anzahl = tk.Label(produktFrame, text="Anzahl", **style.STYLE,
                          activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        anzahl.grid(row=0, column=4, padx=5, pady=3)
        var = IntVar(produktFrame)
        var.set(0)
        self.anzahl_spinbox = tk.Spinbox(produktFrame, width=5, from_=0, to=100, textvariable=var)
        self.anzahl_spinbox.grid(row=0, column=5)


        button1 = tk.Button(produktFrame, text='Löschen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=self.loeschen)
        button1.grid(row=1, column=5, padx=5, pady=3)'''

