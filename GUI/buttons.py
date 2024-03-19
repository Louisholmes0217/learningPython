from tkinter import *

window = Tk() # instantiate an instance of a window
back_colour="#c4c4c4"
#window.geometry("720x720") # geometry allows to select size for window
window.title("button") # setting title of window
window.config(background=back_colour) # setting colour of background

# BUTTON you can click to do something
count = 0
def click():
    global count
    count += 1
    print("counter = {}".format(count))

button = Button(window,                     # assinging button to window
                text="click me",            # text the button contains
                font=("Comic Sans", 30),    # font
                command=click,              # command calls to a function when clicked
                fg="Green",                 # setting foreground text colour
                bg="White",                 # setting background colour
                activebackground="White",   # seting background when clicked colour
                activeforeground="Green",   # setting foreground when clicked colour
                state=ACTIVE                # allows button to be clicked
                )

button.pack()

window.mainloop() # places window on screen, listen for events