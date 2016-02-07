from Tkinter import *

class Application():
    def __init__(self, master):
        print("Applicaiton instance created")
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Just invoked print message")
        
if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
