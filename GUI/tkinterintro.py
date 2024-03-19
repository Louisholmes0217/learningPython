from tkinter import *

# widgets are GUI elements, buttons, text boxes, labels etc.
# windows are a container for elements

##########################################################################
# creating a simple window
window = Tk() # instantiate an instance of a window

back_colour="#c4c4c4"
#car = "C:\\Users\\louis\\Desktop\\Programming\\Python\\GUI\\car.png"
#photo = PhotoImage(file=car)

window.geometry("720x720") # geometry allows to select size for window
window.title("first GUI prog") # setting title of window
#icon = PhotoImage(file="logo.png") converting image to photo
#window.iconphoto(True, icon) # setting icon of window
window.config(background=back_colour) # setting colour of background





#########################################################################
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

########################################################################
# buttons
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
