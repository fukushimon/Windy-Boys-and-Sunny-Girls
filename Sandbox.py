from tkinter import *
import tkinter

########################################## Main window settings ##########################################
root = Tk()

# Window class
class Window:
    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  #  input, sizexsize
        Label(self.root, text=message).pack()

        self.navigationBar = Menu(root)
        self.root.config(menu=self.navigationBar) 

        self.fileMenu = Menu(self.navigationBar, tearoff=0)
        self.navigationBar.add_cascade(label="Datei", menu=self.fileMenu)

        self.fileMenu.add_command(label="Szenario erstellen")
        self.fileMenu.add_command(label="Szenario öffnen")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Schließen", command=self.root.quit)

        self.root.mainloop()
        pass
    pass

class MenuBar(tkinter.Menu):
    def __init__(self, root):
        self.root.config(menu=self)
        fileMenu = self()


# Make window fullscreen
width = 800 # Width 
height = 500 # Height
 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 

mainWindow = Window(root, "Windy Boys and Sunny Girls", '%dx%d+%d+%d' % (width, height, x, y), "Hallo")
# root.title("Windy Boys and Sunny Girls")
# root.iconbitmap("C:/Users/shimo/Desktop/IPJ_Repository/Windy-Boys-and-Sunny-Girls/Images/Logo.ico")

# root.geometry('%dx%d+%d+%d' % (width, height, x, y))

######### Menu bar #########
# navigationBar = mainWindow.Menu(root)
# root.config(menu=navigationBar) 

def openSzenarioWindow():
    pass

def openSzenarioExplorer():
    pass


### Create menu buttons

# "Datei"
# fileMenu = Menu(navigationBar, tearoff=0)
# navigationBar.add_cascade(label="Datei", menu=fileMenu)

# fileMenu.add_command(label="Szenario erstellen", command=openSzenarioWindow)
# fileMenu.add_command(label="Szenario öffnen", command=openSzenarioExplorer)
# fileMenu.add_separator()
# fileMenu.add_command(label="Schließen", command=root.quit)

# # "Ansicht"
# viewMenu = Menu(navigationBar, tearoff=0)
# navigationBar.add_cascade(label="Ansicht", menu=viewMenu)

# viewMenu.add_command(label="Daten einblenden")
# viewMenu.add_command(label="Karte einblenden")

# # Hilfe
# helpMenu = Menu(navigationBar, tearoff=0)
# navigationBar.add_cascade(label="Hilfe", menu=helpMenu)

# # Info
# infoMenu = Menu(navigationBar, tearoff=0)
# navigationBar.add_cascade(label="Info", menu=infoMenu)



# Buttons
class helpIcon(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        # self['bg'] = 'SystemButtonFace'

        self.defaultStyle = PhotoImage(file='images/Help_Icon.png')

        self['image'] = self.defaultStyle
        self['borderwidth'] = 0
        

class basicButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)

        self['bg'] = '#D9D9D9'
        self['borderwidth'] = 0
        self['padx'] = 5
        self['pady'] = 0
        self['bd'] = 1

        # Change color on hover
        def buttonHover(e):
            self['bg'] = '#CFD8E9'
        
        def buttonLeave(e):
            self['bg'] = '#D9D9D9'

        self.bind("<Enter>", buttonHover)
        self.bind("<Leave>", buttonLeave)




def newWindow():
    top = Toplevel()
    window = Window(top, "Hello", "800x200", "Neues Szenario")

button1 = Button(root, text="Increment", command=newWindow)
button1.pack()

helpButton = helpIcon(root).pack(pady=30)
basicButton = basicButton(root, text="Speichern").pack()










root.mainloop()