import turtle as t
import time

class Disc(t.Turtle):
    def __init__(self, height):
        t.Turtle.__init__(self, shape="square", visible=False)
        colorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        self.pu()
        self.ht()
        self.shapesize(1.5, height * 1.5, 4)
        self.fillcolor(colorList[7 - height])
        self.st()


class Tower(list):
    def __init__(self, posX):
        self.posX = posX
    def push(self, disk):
        disk.setpos(self.posX, -150 + (34*len(self)))
        self.append(disk)
    def pop(self):
        disk = list.pop(self)
        disk.sety(150)
        return disk


def hanoi(height, begin, source, destination):
    if height > 0:
        hanoi(height - 1, begin, destination, source)
        destination.push(begin.pop())
        hanoi(height - 1, source, begin, destination)

tower1 = Tower(-250)
tower2 = Tower(0)
tower3 = Tower(250)
for i in range(7, 0, -1):
    tower1.push(Disc(i))
time.sleep(0.5)
hanoi(7, tower1, tower2, tower3)

t.mainloop()