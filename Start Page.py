############# Erste fenster mit datei funktionen #############


try:
    import Tkinter as tk
except:
    import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

#Frame_change
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# Window_Hilfe
    def openHilfe(app):
            newWindow = tk.Toplevel(app)

            newWindow.title("Hilfe")

            newWindow.geometry("400x500")

            tk.Label(newWindow,
                     text="This is Hilfe").pack()

#Window_Info
    def openInfo(app):
        newWindow = tk.Toplevel(app)

        newWindow.title("Information")

        newWindow.geometry("400x500")

        tk.Label(newWindow,
                 text="This is Info").pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to page two",command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.title('Windy boys and Sonny Girls')
    app.geometry('600x300')  # 1500x800
    app.minsize(width=600, height=300)
    app.maxsize(width=1000,height=600)
    app.resizable(width=True, height=True)

# Menu_Bar
    menu_bar = tk.Menu()
    app.config(menu=menu_bar)
    menu_Datei = tk.Menu(menu_bar, tearoff=False)
    menu_Ansicht = tk.Menu(menu_bar, tearoff=False)

# Menu_Options
    menu_bar.add_cascade(label='Datei', menu=menu_Datei)
    menu_bar.add_cascade(label='Ansicht', menu=menu_Ansicht)
    menu_bar.add_command(label='Hilfe',command=app.openHilfe)
    menu_bar.add_command(label='Info', command=app.openInfo)
    menu_bar.add_command(label='Schlie??en', command=app.destroy)

# Options_items
# Datei
    menu_Datei.add_command(label='Hauptseite',command=lambda: app.switch_frame(StartPage))
    menu_Datei.add_command(label='Szenario erstellen',command=lambda: app.switch_frame(PageOne))
    menu_Datei.add_command(label='Szenario ??ffnen',command=lambda: app.switch_frame(PageTwo))
    menu_Datei.add_separator()
    menu_Datei.add_command(label='Schlie??en', command=app.destroy)
# Ansicht
    menu_Ansicht.add_command(label='Daten einblenden')
    menu_Ansicht.add_command(label='Karte einblenden')

    app.mainloop()