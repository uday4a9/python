import Tkinter as kinter
from Tkinter import *

# Create window from here.
window = Tk()

# Create a label and wrap it over the window
"""mylabel = kinter.Label(window, text="Hello, World")
mylabel.pack()
"""

"""
# Create frame form here
# THis is top frame in new window
topframh = Frame()
topframe.pack()

# This is bottom frame in the same window
bottomframe = Frame()
bottomframe.pack(side=BOTTOM)

# Creating any object like Button/Frame will be in two parts.
# 1. Creating it. 2. packing it
button1 = Button(topframe, text="one", fg="red")
button2 = Button(topframe, text="two", fg="green")
button3 = Button(topframe, text="three", fg="yellow")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

button4 = Button(bottomframe, text="four", fg="blue")
button5 = Button(bottomframe, text="five", fg="purple")
button4.pack(side=LEFT)
button5.pack(side=LEFT)
"""

"""
# Create a label and try to fill them in X and Y axis
# Fitting a widget
one = Label(window, text="ONE", fg="red", bg="white")
one.pack()
two = Label(window, text="TWO", fg="green", bg="black")
two.pack(fill=X)
three=Label(window, text="THREE", fg="blue", bg="white")
three.pack(fill=Y, side=RIGHT)
"""

"""
# Create a grid layout for entering the data
l1 = Label(window, text="Name")
l2 = Label(window, text="Password")
l1.grid(row=0, sticky=E)
l2.grid(row=1, sticky=E)

# Read the data from keyboard
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Adding the check button here
c = Checkbutton(window, text="Keep me logged in")
c.grid(columnspan=2)
"""

# Binding and adding the functionality to a button click
def printname():
    print("Hi Uday !!!")

def printnameevent(event):
    print("Hi Uday !!!")

"""
# Below funciton added cooresponding code to invoke printname
button1 = Button(window, text="print the  text", command=printname)
button1.pack()
"""

"""
#We can add the same code wiht the help of event
button1 = Button(window, text="print the text")
button1.bind("<Button-1>", printnameevent)
button1.pack()
"""

# Deal with mouse click events
def leftclick(event):
    print("LEFT")

def middleclick(event):
    print("MIDDLE")

def rightclick(event):
    print("RIGHT")

frame = Frame(window, width=300, height=250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

# Let's run this windod for infinite time
window.mainloop()
