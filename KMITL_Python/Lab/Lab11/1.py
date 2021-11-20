import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def printInfo(self):
        print(f"Position: {self.x}, {self.y};")


class Circle(Point):
    def __init__(self, x = 0, y = 0, radius = 0):
        super().__init__(x, y)

        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius**2)
    
    def printInfo(self):
        print(f"{super().printInfo()} Radius: {self.radius:.2f}; Area: {self.area():.2f};")


class Cylinder(Circle):
    def __init__(self, x = 0, y = 0, radius = 0, height = 0):
        super().__init__(x, y, radius)

        self.height = height

    def area(self):
        return (2 * super().area()) + (2 * math.pi * self.radius + self.height)
    
    def volume(self):
        return super().area() * self.height
    
    def printInfo(self):
        print(f"{super().printInfo()} Height: {self.height:2f}; Volume: {self.volume():.2f};")
