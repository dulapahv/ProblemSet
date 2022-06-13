from tkinter import *
from tkinter import messagebox
import random

class PaintV2:
   def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.canvas = Canvas(mainWindow, width = 450, height = 300)
        self.canvas.grid(row = 1, column = 1)
        self.canvas.create_rectangle(100, 50, 350, 200, outline = '#000000')
        self.canvas.bind("<Motion>", self.draw)
       
   def draw(self, event):
        if (event.x > 100 and event.x < 350) and (event.y > 50 and event.y < 200):
            color = random.randint(0,999999)
            x1 = event.x - 5
            y1 = event.y - 5
            x2 = event.x + 5
            y2 = event.y + 5
            self.canvas.create_oval(x1,y1,x2,y2, fill = '#' + str(color))
        else:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")
       
mainWindow = Tk()
app = PaintV2(mainWindow)
mainWindow.mainloop()