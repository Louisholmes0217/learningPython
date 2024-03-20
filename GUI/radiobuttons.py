from tkinter import *
# similar to checkboxes, but you can only select one in a list

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()
x = StringVar()

def submit():
    print(x.get())

for i in food:
    radiobutton = Radiobutton(window,text=i, variable=x, value=i)
    radiobutton.pack()    

submit_button = Button(window,
                       text="submit",
                        command=submit)

submit_button.pack()
window.mainloop()
