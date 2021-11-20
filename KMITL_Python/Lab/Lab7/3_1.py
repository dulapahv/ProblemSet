from turtle import *

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    # Unable to finish in time. Dismissed and got half a point from TA
    # def intersect(self, rec):
    #     self.x = abs(rec.x - self.x)
    #     self.y = abs(rec.y - self.y)
    #     self.width = rec.width
    #     self.height = rec.height
    
    def draw(self):
        pu()
        goto(self.x, self.y)
        pd()
        for i in range(2):
            fd(self.width)
            rt(90)
            fd(self.height)
            rt(90)

rectangle1 = Rectangle(20,20,100,100)
rectangle2 = Rectangle(40,40,50,50)
rectangle1.draw()
rectangle2.draw()
rectangle1.intersect(rectangle2)
begin_fill()
rectangle1.draw()
end_fill()

done()