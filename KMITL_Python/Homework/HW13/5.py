import tkinter as tk
import math

class Tree:
    def __init__(self):
        window = tk.Tk()
        window.title("Recursive Tree")
        window.resizable(width="false", height="false")

        self.width, self.height = 250, 250
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()

        tk.Label(frame, text="Enter the depth ").grid(row=1, column=1, padx=2)
        self.depth = tk.Entry(frame, width=20, justify = "right")
        self.depth.grid(row=1, column=2)
        tk.Button(frame, text="Display", command=self.display).grid(row=1, column=3)

        window.mainloop()

    def display(self):
        self.canvas.delete(tk.ALL)
        check = min(self.width, self.height) // 3
        self.draw(self.width / 2, self.height - 15, self.width / 2, self.height - 15 - check, 0)

    def draw(self, x0, y0, x1, y1, current):
        self.canvas.create_line(x0, y0, x1, y1)
        if current < int(self.depth.get()):
            x2 = x1 + ((x1 - x0) * math.cos(0.1) - (y1 - y0) * math.sin(1)) / 2
            y2 = y1 + ((y1 - y0) * math.cos(0.1) + (x1 - x0) * math.sin(1)) / 2
            x3 = x1 + ((x1 - x0) * math.cos(0.1) + (y1 - y0) * math.sin(1)) / 2
            y3 = y1 + ((y1 - y0) * math.cos(0.1) - (x1 - x0) * math.sin(1)) / 2

            self.draw(x1, y1, x2, y2, current + 1)
            self.draw(x1, y1, x3, y3, current + 1)


Tree()