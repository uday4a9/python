from Tkinter import *


def donothing():
    print("Call back invoked")

root = Tk()

"""
# create dropdown menu
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New", command=donothing)
submenu.add_command(label="Open", command=donothing)
submenu.add_command(label="Save", command=donothing)
submenu.add_separator()
submenu.add_command(label="close", command=donothing)

editmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=donothing)

# creating toolbar
toolbar = Frame(root, bg="blue")

button1 = Button(toolbar, text="Insert", command=donothing)
button1.pack(side=LEFT, padx=7, pady=3)

button2 = Button(toolbar, text="Delete", command=donothing)
button2.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)

# creating statusbar
statusbar = Label(root, text="To do nothing", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
"""

"""
# creating messagebox
import tkMessageBox

def message():
    tkMessageBox.showinfo("Title", "Info showed up..")
    
def check():
    answer = tkMessageBox.askyesno("Enter choice")
    #print("Result =", answer)
    if answer:
        message()

button = Button(root, text="Press Here", command=check)
button.pack()
"""

"""
# Make shapes
canvas = Canvas(root, width=200, height=100)
canvas.pack()

bline = canvas.create_line(0, 0, 200, 50)
rline = canvas.create_line(0, 100, 200, 50, fill="red")
gbox = canvas.create_rectangle(25, 25, 125, 75, fill="green")

canvas.delete(gbox)
"""

# Add icons and images

fil = r"/home/bujji/Downloads/Eagle Eye (2008)/WWW.YIFY-TORRENTS.COM.jpg"

photo = PhotoImage(file="01.png")
label =Label(root, image=photo)#, text="Click here to get image")
label.pack()

root.mainloop()
