from tkinter import *
from tkinter import messagebox

class KMITL_Phone:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        mainWindow.title("KMITL Phone")

        self.text = Entry(mainWindow, justify = "right", font = ("Arial", 18))
        self.text.grid(row = 1, padx = 8, pady = 8)

        self.oneButton = Button(mainWindow, width = 6, text = "1", font = ("Arial", 18), command = lambda: self.updateText(1))
        self.oneButton.grid(row = 2, sticky = "W")

        self.twoButton = Button(mainWindow, width = 6, text = "2", font = ("Arial", 18), command = lambda: self.updateText(2))
        self.twoButton.grid(row = 2)

        self.threeButton = Button(mainWindow, width = 6, text = "3", font = ("Arial", 18), command = lambda: self.updateText(3))
        self.threeButton.grid(row = 2, sticky = "E")

        self.fourButton = Button(mainWindow, width = 6, text = "4", font = ("Arial", 18), command = lambda: self.updateText(4))
        self.fourButton.grid(row = 3, sticky = "W")

        self.fiveButton = Button(mainWindow, width = 6, text = "5", font = ("Arial", 18), command = lambda: self.updateText(5))
        self.fiveButton.grid(row = 3)

        self.sixButton = Button(mainWindow, width = 6, text = "6", font = ("Arial", 18), command = lambda: self.updateText(6))
        self.sixButton.grid(row = 3, sticky = "E")

        self.sevenButton = Button(mainWindow, width = 6, text = "7", font = ("Arial", 18), command = lambda: self.updateText(7))
        self.sevenButton.grid(row = 4, sticky = "W")

        self.eightButton = Button(mainWindow, width = 6, text = "8", font = ("Arial", 18), command = lambda: self.updateText(8))
        self.eightButton.grid(row = 4)

        self.nineButton = Button(mainWindow, width = 6, text = "9", font = ("Arial", 18), command = lambda: self.updateText(9))
        self.nineButton.grid(row = 4, sticky = "E")

        self.starButton = Button(mainWindow, width = 6, text = "*", font = ("Arial", 18), command = lambda: self.updateText('*'))
        self.starButton.grid(row = 5, sticky = "W")

        self.zeroButton = Button(mainWindow, width = 6, text = "0", font = ("Arial", 18), command = lambda: self.updateText(0))
        self.zeroButton.grid(row = 5)

        self.squareButton = Button(mainWindow, width = 6, text = "#", font = ("Arial", 18), command = lambda: self.updateText('#'))
        self.squareButton.grid(row = 5, sticky = "E")

        self.talkButton = Button(mainWindow, width = 9, text = "Talk", font = ("Arial", 18), command = self.dial)
        self.talkButton.grid(row = 6, sticky = "W")

        self.deleteButton = Button(mainWindow, width = 9, text = "<", font = ("Arial", 18), command = self.delete)
        self.deleteButton.grid(row = 6, sticky = "E")

    def updateText(self, char):
        self.text.insert(END, char)
    
    def dial(self):
        messagebox.showinfo("Dial", "Dialing <<%s>>" % self.text.get())

    def delete(self):
        self.text.delete(len(self.text.get()) - 1, END)

mainWindow = Tk()
app = KMITL_Phone(mainWindow)
mainWindow.mainloop()