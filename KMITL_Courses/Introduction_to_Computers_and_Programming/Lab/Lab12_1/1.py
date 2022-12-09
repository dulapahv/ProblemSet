from turtle import *
from abc import ABC, abstractmethod

speed(0)

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self):
        pu()
        setpos(self.x1, self.y1)
        pd()
        setpos(self.x2, self.y2)


class Rectangle(TwoDShape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        pu()
        setpos(self.x, self.y)
        pd()
        for i in range(2):
            fd(self.width)
            rt(90)
            fd(self.height)
            rt(90)


class Circle(TwoDShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        pu()
        setpos(self.x, self.y)
        pd()
        circle(self.radius)


r1 = Rectangle(100, 200, 50, 30)
r1.draw()
l1 = Line(5, 10, 55, 65)
l1.draw()
c1 = Circle(-100, -100, 50)
c1.draw()
l2 = Line(-55, 10, -55, 100)
l2.draw()
c2 = Circle(100, -200, 90)
c2.draw()
mainloop()