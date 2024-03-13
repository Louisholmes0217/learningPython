# This is an app to messa round with tkinter basics

import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x200")
        self.root.title("Text app")
        self.mainframe = tk.Frame(self.root, background="white")
        self.mainframe.pack(fill="both", expand=True)

        self.text = ttk.Label(self.mainframe, text="This is my text", background="white", font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky="NWES")

        set_text_button = ttk.Button(self.mainframe, text="set text", command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)

        colour_options = ["red", "blue", "green", "black"]
        self.set_colour_field = ttk.Combobox(self.mainframe, values=colour_options)
        self.set_colour_field.grid(row=2, column=0, sticky="NWES", pady=10)
        
        self.set_colour_button = ttk.Button(self.mainframe, text="Set colour", command=self.set_colour)
        self.set_colour_button.grid(row=2, column=1, pady=10)

        self.reverse_text = ttk.Button(self.mainframe, text="Reverse Text", command=self.reverse)
        self.reverse_text.grid(row=3, column=0, sticky="NWES", pady=10)

        self.root.mainloop()
        return
    
    def reverse(self):
        newtext = self.text.cget("text")
        reversed = newtext[::-1]
        self.text.config(text=reversed)

    def set_colour(self):
        newcolour = self.set_colour_field.get()
        self.text.config(foreground=newcolour)
    
    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

if __name__ == '__main__':
    App()