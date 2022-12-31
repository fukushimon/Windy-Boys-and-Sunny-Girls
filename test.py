# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class Input_Class:

    def __init__(self, get_dictionary=None, set_dictionary=None):

        if get_dictionary:
            self.get_dictionary = get_dictionary
        else:
            self.dictionary = {
                'Name': '',
                'Vorname': '',
                'Straße': '',
                'Hausnummer': '',
                'PLZ': '',
                'Ort': '',
            }
            self.get_dictionary = self.get_own_dictionary

        if set_dictionary:
            self.set_dictionary = set_dictionary
        else:
            self.set_dictionary = self.set_own_dictionary

    def get_own_dictionary(self):
        return self.dictionary

    def set_own_dictionary(self, **kwargs):
        for key in kwargs:
            self.dictionary[key] = kwargs[key]

    def config(self, **kwargs):
        if kwargs:
            self.set_dictionary(**kwargs)
        return self.get_dictionary()

    def __getitem__(self, key):
        return self.config()[key]

    def __setitem__(self, key, value):
        self.config(**{key: value})

    def keys(self):
        return ['Name',
                'Vorname',
                'Straße',
                'Hausnummer',
                'PLZ',
                'Ort',
                ]


class Application(tk.Tk):

    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        # widget definitions ===================================
        self.Eingabemaske = Eingabemaske(self)
        self.Eingabemaske.pack(fill='x')

        self.Eingabemaske.create_Eingabemaske(Input_Class())


class Eingabemaske(tk.LabelFrame):

    def __init__(self, master, **kwargs):
        tk.LabelFrame.__init__(self, master, **kwargs)
        self.config(text='Eingabemaske')
        # widget definitions ===================================
        self.content = tk.Frame(self)
        self.content.pack(fill='x')

    def create_Eingabemaske(self, input_object):
        keys = input_object.keys()

        maxlen = 0
        for key in keys:
            maxlen = max(maxlen, len(key))

        self.content.destroy()
        self.content = tk.Frame(self)
        self.content.pack(fill='x')

        entrylist = []  # Liste mit den Eingabefeldern zum Speichern

        for key in keys:
            frame = tk.Frame(self.content)
            frame.pack(fill='x')
            label = tk.Label(frame, text=key, width=maxlen + 1, anchor='e')
            label.pack(side='left')

            # Sonderbehandlung für spezielle Eingabefelder
            if key == 'PLZ':
                width = 5
                expand = 0
                fill = None
            elif key == 'Hausnummer':
                width = 6
                expand = 0
                fill = None
            else:
                width = 30
                expand = 1
                fill = 'x'
            # ===========================================

            entry = tk.Entry(frame, width=width)

            entry.key = key  # das ist zum Speichern
            entrylist.append(entry)  # und das auch

            entry.delete(0, 'end')
            entry.insert(0, str(input_object[key]))
            entry.pack(side='left', fill=fill, expand=expand, padx=5, pady=1)

        def save_input():
            for entry in entrylist:
                input_object[entry.key] = str(entry.get())

            # Zum Anschauen =============================
            print(input_object.config())

        okbutton = tk.Button(self.content, text='OK')
        okbutton.pack(anchor='e')
        okbutton['command'] = save_input


if __name__ == '__main__':
    Application().mainloop()