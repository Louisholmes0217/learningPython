from tkinter import *
window = Tk() # instantiate an instance of a window
window.geometry("300x100")

def display():      # function runs when the checkbox is toggled
    if(x.get()==1):
        print("You agree!")
    else:
        print("You dont agree :c")

x = IntVar()    # special tkinter way of storing a value from checkbox, can be stringVar or boolVar
check_button = Checkbutton(window,
                           text="I aggree to this thing",
                           variable=x,  # variable modified by this box
                           onvalue=1,   # value of x when checked
                           offvalue=0,  # value of x when unchecked
                           command=display, # function to run when toggled
                           font=("Arial", 20),
                           fg=("black"),
                           bg=("gray"),
                           activebackground=("gray"),
                           activeforeground=("black"))
check_button.pack()
window.mainloop()
