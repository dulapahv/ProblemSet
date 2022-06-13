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


class Square(TwoDShape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    
    def draw(self):
        pu()
        setpos(self.x, self.y)
        pd()
        for i in range(4):
            fd(self.side)
            rt(90)


s1 = Square(100, -100, 40)
s1.draw()
s2 = Square(-100, -100, 60)
s2.draw()
s3 = Square(100, 100, 100)
s3.draw()
s4 = Square(-100, 100, 50)
s4.draw()
mainloop()