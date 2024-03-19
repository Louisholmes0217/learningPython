from tkinter import *

window = Tk() # instantiate an instance of a window
back_colour="#c4c4c4"
#window.geometry("720x720") # geometry allows to select size for window
window.title("button") # setting title of window
window.config(background=back_colour) # setting colour of background

# setting widgets
# LABEL is an area widget that holds text/image within a window
label = Label(
    window,
    text="Hello",
    font=("Arial",40,"bold"),
    background=back_colour,
    foreground="Red",
    relief=RAISED,
    bd=14,
    padx=20,
    pady=20,
    #image=photo,
    #compound="bottom"
    ) # There are many arguments you can give to the label to alter its design

label.pack() # This adds the label to the window
#label.place(x=200,y=200) # this adds in a specific place

window.mainloop()