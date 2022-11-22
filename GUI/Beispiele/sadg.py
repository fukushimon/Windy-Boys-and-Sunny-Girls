#img1 = Image.open('Bilder/HHcopy.png').resize((900, 350))
#img2 = Image.open('Bilder/SHcopy.png').resize((900, 350))
import tkinter as tk
from PIL import Image,ImageTk
from random import randint, randrange
import time

# --- classes ---

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master, bg="")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create empty label
        self.arrow = tk.Label(self)
        self.arrow.pack()

    def update_image(self, img):
        # set image in label
        self.arrow.config(image=img)

        # because image is assigned to global list `imgs`
        # so this command may not be needed
        self.arrow.image = img

# --- functions ---

def classifier():
    # return randint(0, len(imgs)-1) # with -1
    return randrange(0, len(imgs))   # without -1

def update_loop():
    # run your classifier from other file
    selected = classifier()

    # get image from list
    img = imgs[selected]

    # update image in window
    app.update_image(img)

    # run it again after 4000ms
    root.after(4000, update_loop)

# --- main ---

root = tk.Tk()

# list with images (create after creating `root`)
imgs = [ImageTk.PhotoImage(Image.open('Bilder/HHcopy.png')), ImageTk.PhotoImage(Image.open('Bilder/SHcopy.png'))]

# creacte app
app = Application(root)

# run it first time
update_loop()

# start "engine"
app.mainloop()