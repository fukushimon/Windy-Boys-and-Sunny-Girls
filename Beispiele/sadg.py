import tkinter as tk
from tkinter import messagebox as msg

my_w = tk.Tk()
my_w.geometry("500x300")  # Size of the window
my_val = ''


def my_upd():
    # print(r1_v.get())
    if (r1_v.get() == 1):
        my_title = "Value = 1"
        my_msg = "Default Selection is Yes"
        my_button = "yes"
    elif (r1_v.get() == 2):
        my_title = "Value = 2"
        my_msg = "Default Selection is No"
        my_button = "no"
    elif (r1_v.get() == 3):
        my_title = "Value = 3"
        my_msg = "Default Selection is Cancel"
        my_button = "cancel"

    my_val = msg.askyesnocancel(my_title, my_msg, default=my_button)


r1_v = tk.IntVar()  # We used integer variable here

r1 = tk.Radiobutton(my_w, text='Yes', variable=r1_v, value=1, command=my_upd)
r1.grid(row=1, column=1)

r2 = tk.Radiobutton(my_w, text='No', variable=r1_v, value=2, command=my_upd)
r2.grid(row=1, column=2)

r3 = tk.Radiobutton(my_w, text='Cancel', variable=r1_v, value=3, command=my_upd)
r3.grid(row=1, column=3)

my_w.mainloop()