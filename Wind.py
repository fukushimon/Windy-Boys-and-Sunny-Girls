import tkinter as tk
from tkinter import *
from tkinter import messagebox

import Energiebilanz
import Speicher
import Home
import Solar
from Windmaske import ProduktFrameWind
from konstante import style
from konstante.Product import LIST_WIND, LIST_SOLAR, LIST_SPEICHER, REFERENCE, HERSTELLER_WIND, MODELL_WIND, \
    STANDORT_WIND, ANZAHL_WIND, HERSTELLER_SOLAR, MODELL_SOLAR, STANDORT_SOLAR, FLAECHE_SOLAR, ANLAGE_SPEICHER, \
    ANZAHL_SPEICHER, FAKTOREN_LIST


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
        self.windFrame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=8)

        # Scrollbar hinzufügen
        self.canvas = tk.Canvas(self.windFrame, background=style.BACKGROUND)
        scrollbar = tk.Scrollbar(self.windFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, background=style.BACKGROUND)


        self.scrollable_frame.bind(
        #self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind('<Enter>', self._bind_to_mousewheel)
        self.scrollable_frame.bind('<Leave>', self._unbind_from_mousewheel)

        self.canvas.create_window((0, 0), anchor="nw", window=self.scrollable_frame)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

#Beschreibung Szenario
        self.szenario_beschreibung()

# Wind-Produkte
        self.add_produktFrame()

    def szenario_beschreibung(self):
        datenFrame = tk.Frame(self.scrollable_frame)
        datenFrame.config(background=style.BACKGROUND)
        datenFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8)
        datenFrame.grid_columnconfigure(1, weight=1)
        datenFrame.grid_columnconfigure(3, weight=1)
        datenFrame.grid_columnconfigure(5, weight=1)

        label_Szenarioname = tk.Label(datenFrame, text='Szenarioname:', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioname.grid(row=0, column=0, padx=5, pady=3)
        self.txt_name = tk.Entry(datenFrame, width=50)
        self.txt_name.grid(row=0, column=1, padx=5, pady=3)

        label_Szenariojahr = tk.Label(datenFrame, text='Szenario für: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariojahr.grid(row=0, column=2, padx=5, pady=3)
        self.txt_jahr = tk.Entry(datenFrame, width=25)
        self.txt_jahr.grid(row=0, column=3, padx=5, pady=3)

        label_Szenariobudget = tk.Label(datenFrame, text='Budget: ', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenariobudget.grid(row=0, column=4, padx=5, pady=3)
        self.txt_budget = tk.Entry(datenFrame, width=40)
        self.txt_budget.grid(row=0, column=5, padx=5, pady=3)
        label_Szenarioeuro = tk.Label(datenFrame, text='EURO', **style.STYLE,
                              activebackground=style.BACKGROUND, activeforeground=style.TEXT)
        label_Szenarioeuro.grid(row=0, column=6, padx=5, pady=3)
        uebernehmen_bto = tk.Button(datenFrame, text='Daten übernehmen', **style.STYLE, activebackground=style.BACKGROUND,
                                    activeforeground=style.TEXT, command=lambda: self.daten_eingabe())
        uebernehmen_bto.grid(row=0, column=7, padx=5, pady=3)

    def daten_eingabe(self):
        REFERENCE.clear()
        REFERENCE.insert(0, self.txt_name.get())
        REFERENCE.insert(1, self.txt_jahr.get())
        REFERENCE.insert(2, self.txt_budget.get())
        print(REFERENCE)

        #Solar.Solar.daten_szenario(self)
        #Solar.Solar.update(self)
        #self.name.update()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")


    def leistung(self):
        leistungFrame = tk.Frame(self)
        leistungFrame.config(background=style.BACKGROUND)
        leistungFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=8)
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
        anlage_button.grid(row=0, column=4, padx=5, pady=3, sticky=EW)

        berechnen = tk.Button(leistungFrame, text='Berechnen', **style.STYLE, activebackground=style.BACKGROUND,
                              activeforeground=style.TEXT, command=lambda: Wind.faktoren_beruecksichtigen(self))
        berechnen.grid(row=0, column=6, padx=5, pady=3)
        Speichern = tk.Button(leistungFrame, text='Speichern', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT)
        Speichern.grid(row=0, column=7, padx=5, pady=3)
        schliessen = tk.Button(leistungFrame, text='Schließen', **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT, command=lambda: self.controller.show_frame(Home.Home))
        schliessen.grid(row=0, column=8, padx=5, pady=3)

    def add_produktFrame(self):
        produktFrame = ProduktFrameWind(self.scrollable_frame)
        produktFrame.config(background=style.BACKGROUND)
        produktFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=8, expand=True)

        LIST_WIND.append(produktFrame)

    def faktoren_beruecksichtigen(self):
        self.newWindow = tk.Toplevel(self)
        self.newWindow.title("Berechnen")
        self.newWindow.geometry("400x500")
        self.newWindow.config(bg=style.BACKGROUND)
        tk.Label(self.newWindow, text="Faktoren zu berücksichtigen ", **style.STYLE, activebackground=style.BACKGROUND,
                 activeforeground=style.TEXT).grid(row=0, columnspan=2, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Wetterdaten: ", **style.STYLE, activebackground=style.BACKGROUND,
                 activeforeground=style.TEXT).grid(row=1, columnspan=1, sticky=W, padx=5, pady=3)

        self.option1 = IntVar()
        self.option1.set(0)
        Radiobutton(self.newWindow, text="(2020/2021", variable=self.option1, value=0, **style.STYLE,
                    activebackground=style.BACKGROUND, activeforeground=style.TEXT).\
            grid(row=2, column=0, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="2022", variable=self.option1, value=1, **style.STYLE,
                    activebackground=style.BACKGROUND,activeforeground=style.TEXT).\
            grid(row=2, column=1, sticky=W, padx=5, pady=3)
        tk.Label(self.newWindow, text="Globalstrahlungsfaktor", **style.STYLE, activebackground=style.BACKGROUND,
                 activeforeground=style.TEXT).grid(row=3, columnspan=1, sticky=W, padx=5, pady=3)

        self.option2 = IntVar()
        self.option2.set(0)
        Radiobutton(self.newWindow, text="Ja", variable=self.option2, value=0, **style.STYLE,
                    activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=4, column=0, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="Nein", variable=self.option2, value=1, **style.STYLE,
                    activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=4, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Repowering", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=5, columnspan=1, sticky=W, padx=5, pady=3)

        self.option3 = IntVar()
        self.option3.set(0)
        Radiobutton(self.newWindow, text="Ja", variable=self.option3, value=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=6, column=0, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="Nein", variable=self.option3, value=1, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=6, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Verbaruchsszenarien", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=7, columnspan=1, sticky=W, padx=5, pady=3)

        self.option4 = IntVar()
        self.option4.set(0)
        Radiobutton(self.newWindow, text="Bundesregierung", variable=self.option4, value=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=8, column=0, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="alles bleibt gleich", variable=self.option4, value=1, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=8, column=1, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="Sektorenkopplung", variable=self.option4, value=2, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=9, column=0, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="PR-Faktor verändern?", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=10, columnspan=1, sticky=W, padx=5, pady=3)

        self.option5 = IntVar()
        self.option5.set(0)
        Radiobutton(self.newWindow, text="Ja", variable=self.option5, value=0, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=11, column=0, sticky=W, padx=5, pady=3)
        Radiobutton(self.newWindow, text="Nein", variable=self.option5, value=1, **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=11, column=1, sticky=W, padx=5, pady=3)
        #option10 = IntVar()
        #option11 = IntVar()
        #Checkbutton(self.newWindow, text="Ja", variable=option10, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
        #                    activeforeground=style.TEXT).grid(row=11, column=0, sticky=W, padx=5, pady=3)
        #Checkbutton(self.newWindow, text="Nein", variable=option11, onvalue=1, offvalue=0, **style.STYLE, activebackground=style.BACKGROUND,
        #                    activeforeground=style.TEXT).grid(row=11, column=1, sticky=W, padx=5, pady=3)

        tk.Label(self.newWindow, text="Startwert  der Speicher in % : ", **style.STYLE, activebackground=style.BACKGROUND,
                            activeforeground=style.TEXT).grid(row=12, columnspan=1, sticky=W, padx=5, pady=3)

        self.ladung = IntVar(self.newWindow)
        self.ladung.set(0)
        self.ladung_spinbox = tk.Spinbox(self.newWindow, width=5, from_=0, to=100, textvariable=self.ladung)
        self.ladung_spinbox.grid(row=13, sticky=W, padx=5, pady=3)

        weiter_button = tk.Button(self.newWindow, text='Weiter', **style.STYLE,
                               activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                               command=lambda: Wind.berechnen(self))
        weiter_button.grid(row=14, column=0, sticky=E, padx=5, pady=3)

        abbrechen_button = tk.Button(self.newWindow, text='Abbrechen', **style.STYLE,
                               activebackground=style.BACKGROUND, activeforeground=style.TEXT,
                               command=lambda: self.newWindow.destroy())
        abbrechen_button.grid(row=14, column=1, sticky=E, padx=5, pady=3)

    def berechnen(self):
        confirm = messagebox.askyesnocancel('Berechnung', 'Alle zuvor ausgewählten Faktoren werden für die Berechnungsoperation berücksichtigt. \nWenn Sie die Faktoren erneut ändern möchten, klicken Sie auf Abbrechen')
        if confirm:
            FAKTOREN_LIST.clear()
            FAKTOREN_LIST.append([self.option1.get(), self.option2.get(), self.option3.get(), self.option4.get(), self.option5.get(), self.ladung.get()])
            print(FAKTOREN_LIST)


            wind = 1
            solar = 1
            speicher = 1
            for frame in LIST_WIND:
                print('--------------------------')
                print('Wind-Product', wind)
                print('--------------------------')
                print(frame.cbx_hersteller.get())
                print(frame.cbx_modellname.get())
                print(frame.anzahl.get())
                print(frame.cbx_standort.get())
                print()
                wind += 1
            # Liste für Shimon
            for frame in LIST_WIND:
                HERSTELLER_WIND.clear()
                MODELL_WIND.clear()
                STANDORT_WIND.clear()
                ANZAHL_WIND.clear()

                HERSTELLER_WIND.append(frame.cbx_hersteller.get())
                MODELL_WIND.append(frame.cbx_modellname.get())
                STANDORT_WIND.append(frame.cbx_standort.get())
                ANZAHL_WIND.append(frame.anzahl.get())

            for frame in LIST_SOLAR:
                print('--------------------------')
                print('Solar-Product', solar)
                print('--------------------------')
                print(frame.cbx_hersteller.get())
                print(frame.cbx_modellname.get())
                print(frame.anzahl.get())
                print(frame.cbx_standort.get())
                print()
                solar += 1
            # Liste für Shimon
            for frame in LIST_SOLAR:
                HERSTELLER_SOLAR.clear()
                MODELL_SOLAR.clear()
                STANDORT_SOLAR.clear()
                FLAECHE_SOLAR.clear()

                HERSTELLER_SOLAR.append(frame.cbx_hersteller.get())
                MODELL_SOLAR.append(frame.cbx_modellname.get())
                STANDORT_SOLAR.append(frame.cbx_standort.get())
                FLAECHE_SOLAR.append(frame.anzahl.get())

            for frame in LIST_SPEICHER:
                print('--------------------------')
                print('Speicher-Product', speicher)
                print('--------------------------')
                print(frame.lbl1['text'])
                print(frame.anzahl.get())
                print()
                speicher += 1
            # Liste für Shimon
            for frame in LIST_SPEICHER:
                ANLAGE_SPEICHER.clear()
                ANZAHL_SPEICHER.clear()

                ANLAGE_SPEICHER.append(frame.lbl1['text'])
                ANZAHL_SPEICHER.append(frame.anzahl.get())

            print(HERSTELLER_WIND)
            print(MODELL_WIND)
            print(STANDORT_WIND)
            print(ANZAHL_WIND)
            print(HERSTELLER_SOLAR)
            print(ANLAGE_SPEICHER)
            
            self.controller.show_frame(Energiebilanz.Energiebilanz)
            self.newWindow.destroy()
        elif confirm is None:
            self.newWindow.destroy()
            self.faktoren_beruecksichtigen()
        else:
            self.newWindow.destroy()

