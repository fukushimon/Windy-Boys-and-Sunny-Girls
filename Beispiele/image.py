import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry('1500x600')

image = Image.open('../Bilder/HHcopy.png')#.resize((300, 200))
photo = ImageTk.PhotoImage(image)

label1 = tk.Label(root, text='das ist unsere logo', image=photo, compound='top')
label1.pack()

label1.configure(background='red') # um weiteren anpassungen zu machen

#style = ttk.Style()   für apple
#style.theme_use('clam')  für apple
for item in label1.keys(): # damit kann ich sehen alles was ich ändern kann
    print(item, ':', label1[item])

label1['image'] = photo

root.mainloop()


#abschnitt 8 1:18:58
