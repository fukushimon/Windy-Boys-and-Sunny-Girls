import tkinter as tk
from tkinter import messagebox

class SeleccionColor(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Selección Color')
        self.geometry('300x300')

        self.color_seleccionado = tk.StringVar(self)
        self.color_seleccionado.set('2020')

        Energiedaten = [('2020', '2020'), ('2021', 'verde'), ('2022', 'azul')]

        opciones_color = [self.crear_opcion(c) for c in Energiedaten]

        for o in opciones_color:
            o.pack()

    def crear_opcion(self, c):
        texto, valor = c

        return tk.Radiobutton(self, text=texto, value=valor, command=self.mostrar_seleccion, variable=self.color_seleccionado)

    def mostrar_seleccion(self):
        messagebox.showinfo('Info', f'Ausgewählte Energiedaten "momentan farbe": {self.color_seleccionado.get()}')


def main():
    app = SeleccionColor()
    app.mainloop()


if __name__ == '__main__':
    main()