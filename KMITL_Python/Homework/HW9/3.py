from tkinter import *

class Circle:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.tag = 0
    
        self.canvas = Canvas(mainWindow, width = 500, height = 300, bg = "white")
        self.canvas.grid(row = 1, column = 1)
        self.canvas.bind('<Button-1>', self.addCircle)
        self.canvas.bind('<Button-3>', self.removeCircle)
    
    def addCircle(self, event):
        tag = str(self.tag)
        self.canvas.create_oval(event.x + 25, event.y + 25, event.x - 25, event.y - 25, tag = tag)
        self.tag += 1

    def removeCircle(self, event):
        tag = self.canvas.find_closest(event.x, event.y)
        self.canvas.delete(tag)


mainWindow = Tk()
app = Circle(mainWindow)
mainWindow.mainloop()