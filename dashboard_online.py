# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('600x780')

# adding a label to the root window
lbl = Label(root, text="Are you a Geek?")
lbl.grid()


# function to display text when
# button is clicked
def clicked():
    lbl.configure(text="I just got clicked")


# button widget with red color text
# inside
btn = Button(root, text="Click me",
             fg="red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)



# all widgets will be here
# Execute Tkinter
root.mainloop()
