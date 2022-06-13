from tkinter import *

class Paint:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        mainWindow.title("A simple paint program")
        
        self.canvas = Canvas(mainWindow, width = 500, height = 500)
        self.canvas.grid(row = 1, column = 1)
        self.canvas.bind('<B1-Motion>', self.draw)

        text = Label(mainWindow, text = "Drag the mouse to draw")
        text.grid(row = 2, column = 1)

        clearButton = Button(mainWindow, text = "Clear", width = 80, command = self.clear)
        clearButton.grid(row = 3, column = 1)

    def draw(self, event):
        x1 = event.x - 5
        y1 = event.y - 5
        x2 = event.x + 5
        y2 = event.y + 5
        self.canvas.create_oval(x1,y1,x2,y2, fill = "#000000")
       
    def clear(self):
        self.canvas.delete("all")

mainWindow = Tk()
app = Paint(mainWindow)
mainWindow.mainloop()