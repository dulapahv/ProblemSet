from turtle import *
speed(0)
ht()


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pu()
        setpos(self.x * 10, self.y * 10)
        pd()
        dot(6)

    def getPosition(self):
        return f"{self.x}, {self.y}"


class Rectangle2D(Point):
    def __init__(self, maxX, maxY, minX, minY):
        super().__init__((maxX + minX) / 2, (maxY + minY) / 2)
        self.maxX = maxX
        self.maxY = maxY
        self.minX = minX
        self.minY = minY

    def draw(self):
        pu()
        setpos(self.minX * 10, self.maxY * 10)
        pd()
        setpos(self.maxX * 10, self.maxY * 10)
        setpos(self.maxX * 10, self.minY * 10)
        setpos(self.minX * 10, self.minY * 10)
        setpos(self.minX * 10, self.maxY * 10)

    def getWidth(self):
        return self.maxX - self.minX

    def getHeight(self):
        return self.maxY - self.minY


def getRectangle(points):
    x = []
    y = []
    for coordinate in range(len(points)):
        if coordinate % 2 == 1:
            y.append(float(points[coordinate]))
        elif coordinate % 2 == 0:
            x.append(float(points[coordinate]))
    for i in range(min(len(x), len(y))):
        point = Point(x[i], y[i])
        point.draw()
        points.append(point)
        point.getPosition()
    rectangle = Rectangle2D(max(x), max(y), min(x), min(y))
    rectangle.draw()
    print(f"The bounding rectangle is centered at ({rectangle.getPosition()}) with width {rectangle.getWidth()} and height {rectangle.getHeight()}")

def main():
    xy = input("Enter the points: ").split()
    getRectangle(xy)

main()
mainloop()