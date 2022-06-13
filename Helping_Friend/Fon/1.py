import turtle
from abc import ABC, abstractmethod
t = turtle.Turtle()

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        t.pu()
        t.goto(self.x1, self.y1)
        t.pd()
        t.goto(self.x2, self.y2)


class Rectangle(TwoDShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)


class Circle(TwoDShape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        t.circle(self.radius)


class Square(TwoDShape):
    def __init__(self, length):
        self.l = length

    def draw(self):
        for i in range(4):
            t.fd(self.l)
            t.rt(90)
turtle.done()

turtle.mainloop()