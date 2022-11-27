import pandas as pd
import tkinter as tk
from tkinter import ttk



class DataFrameTreeView(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree_view = None
        self.hscrollbar = None
        self.vscrollbar = None

    def load_table(self, df, columns=None, columns_headers=None, chunk_size=100):
        """
        Args:
            path: cadena -> ruta al fichero .xlsx
            columns: list -> columnas a mostrar en la tabla, si es None se,muestran todas
            columns_headers: list -> Nombres para las cabeceras de las columnas,
                                     si es None se usan las cabeceras del DataFrame

            chunk_size: int -> Número de filas creadas por iteración
        """

        if columns is not None:
            dif = set(columns) - set(df.columns)
            if dif:
                raise ValueError(f"Columns: {tuple(dif)} are not in DataFrame")
        else:
            columns = df.columns

        if columns_headers is not None:
            if  len(columns_headers) != len(df.columns):
                raise ValueError("headers length not mismath columns number")
        else:
            columns_headers = columns
        tk_col_names =[f"#{name}" for name in columns_headers]

        # Treeview y barras
        if self.tree_view is not None:
            self.tree_view.destroy()
            self.hscrollbar.destroy()
            self.vscrollbar.destroy()

        self.tree_view = ttk.Treeview(self, columns=tk_col_names)
        self.vscrollbar = ttk.Scrollbar(self, orient='vertical', command = self.tree_view.yview)
        self.vscrollbar.pack(side='right', fill=tk.Y)
        self.hscrollbar = ttk.Scrollbar(self, orient='horizontal', command = self.tree_view.xview)
        self.hscrollbar.pack(side='bottom', fill=tk.X)
        self.tree_view.configure(yscrollcommand=self.vscrollbar.set)
        self.tree_view.configure(xscrollcommand=self.hscrollbar.set)

        # Configuar columnas y cabeceras
        for name, header in zip(tk_col_names, columns_headers):
            self.tree_view.column(name, anchor=tk.W)
            self.tree_view.heading(name, text=header, anchor=tk.W)

        # Cargamos los items
        rows = df.shape[0]
        chunks = rows / chunk_size
        progress = 0
        step = 100 / chunks

        progress_bar = ttk.Progressbar(self, orient="horizontal",
                                        length=100, mode="determinate")
        progress_bar["value"] = progress
        label = tk.Label(self, text="Cargando filas")
        label.place(relx=0.50, rely=0.45, anchor=tk.CENTER)
        progress_bar.place(relx=0.5, rely=0.5, relwidth=0.80,  anchor=tk.CENTER)

        for ind in df.index:
            values = [str(v) for v in df.loc[ind, columns].values]
            self.tree_view.insert("", tk.END, text=ind+1, values=values)
            if ind % chunk_size == 0:
                self.update_idletasks()
                progress += step
                progress_bar["value"] = progress

        progress_bar["value"] = progress
        self.update_idletasks()

        progress_bar.destroy()
        label.destroy()
        self.tree_view.pack(expand=True, fill='both')
        #self.tree_view['show'] = 'headings'


class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.geometry("600x500")
        self.button = tk.Button(self, text="Cargar datos", command=self.on_button_clicked)
        self.button.pack()
        self.treeview = DataFrameTreeView(self)
        self.treeview.pack(expand=True, fill='both')


    def on_button_clicked(self):
        self.button.configure(state=tk.DISABLED)
        columns_headers = [f"Columna {n}" for n in range(1, 19)]
        dataframe = pd.read_excel("WEA in Hamburg.xlsx")
        self.treeview.load_table(dataframe, columns_headers=columns_headers)
        self.button.configure(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack(expand=True, fill='both')
    root.mainloop()