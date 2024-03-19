from tkinter import *

window = Tk() # instantiate an instance of a window
back_colour="#c4c4c4"
window.title("entry") # setting title of window
window.config(background=back_colour) # setting colour of background





def submit():                       # callback funtion for our entry button
    entered_text = entry.get()      # get method grabs what is in an entry object
    print(entered_text) 
    #entry.config(state=DISABLED)     

def delete():
    entry.delete(0, END)                  # takes starting point and end point as args for deletion

def backspace():
    entry.delete(len(entry.get())-1, END) # deletes last character in entrybox



entry = Entry(window,               # simple entry window
              font=("Arial", 50),
              bg=back_colour,
              fg="black",
              show="*")

#entry.insert(0,"chad")

submit_button = Button(window,
                       text="Submit entry",
                       command=submit)
delete_button = Button(window,
                       text="Delete",
                       command=delete)
backspace_button = Button(window,
                       text="Backspace",
                       command=backspace)


backspace_button.pack()
delete_button.pack()
entry.pack(side=LEFT)
submit_button.pack(side=RIGHT)
window.mainloop() # places window on screen, listen for events
