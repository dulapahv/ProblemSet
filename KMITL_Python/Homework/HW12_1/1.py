import turtle as t
from abc import ABC, abstractmethod

t.speed(0)
t.ht()


class Char(ABC):
    @abstractmethod
    def __init__(self, width):
        self.width = width

    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        return self.width


class Char0(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        for i in range(2):
            t.fd(super().getWidth())
            t.lt(90)
            t.fd(super().getWidth() * 1.5)
            t.lt(90)
    
    def getWidth(self):
        return self.width()


class Char1(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        t.fd(super().getWidth())
        t.lt(180)
        t.fd(super().getWidth() / 2)
        t.rt(90)
        t.fd(super().getWidth() * 1.5)
        t.lt(135)
        t.fd(super().getWidth() / 3)

    def getWidth(self):
        return self.width()


class Char2(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        t.fd(super().getWidth())
        t.bk(super().getWidth())
        t.lt(90)
        t.fd(super().getWidth() * 0.75)
        t.rt(90)
        t.fd(super().getWidth())
        t.lt(90)
        t.fd(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char3(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        t.fd(super().getWidth())
        t.lt(90)
        t.fd(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())
        t.bk(super().getWidth())
        t.rt(90)
        t.fd(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char4(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x ,y)
        t.seth(0)
        t.fd(super().getWidth())
        t.pd()
        t.lt(90)
        t.fd(super().getWidth() * 1.5)
        t.bk(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())
        t.rt(90)
        t.fd(super().getWidth() * 0.75)

    def getWidth(self):
        return self.width()


class Char5(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        t.fd(super().getWidth())
        t.lt(90)
        t.fd(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())
        t.rt(90)
        t.fd(super().getWidth() * 0.75)
        t.rt(90)
        t.fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char6(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        t.fd(super().getWidth())
        t.lt(90)
        t.fd(super().getWidth() * 0.75)
        t.lt(90)
        t.fd(super().getWidth())
        t.rt(90)
        t.fd(super().getWidth() * 0.75)
        t.bk(super().getWidth() * 1.5)

    def getWidth(self):
        return self.width()


class Char7(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.fd(super().getWidth())
        t.pd()
        t.lt(90)
        t.fd(super().getWidth() * 1.5)
        t.lt(90)
        t.fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char8(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.pd()
        for i in range(2):
            for j in range(2):
                t.fd(super().getWidth())
                t.lt(90)
                t.fd(super().getWidth() * 0.75)
                t.lt(90)
            t.lt(90)
            t.fd(super().getWidth() * 0.75)
            t.rt(90)

    def getWidth(self):
        return self.width()


class Char9(Char):
    def __init__(self, width):
        super().__init__(width)
    
    def draw(self, x, y):
        t.pu()
        t.setpos(x, y)
        t.seth(0)
        t.fd(super().getWidth())
        t.pd()
        t.lt(90)
        t.fd(super().getWidth() * 1.5)
        for i in range(2):
            t.lt(90)
            t.fd(super().getWidth())
            t.lt(90)
            t.fd(super().getWidth() * 0.75)

    def getWidth(self):
        return self.width()


def drawNum(x):
    x = str(x)
    size = 50
    posX, posY = 0 - (30 * len(x)), 0
    numDict = {"0": Char0(size), "1": Char1(size), "2": Char2(size), "3": Char3(size), "4": Char4(size), 
           "5": Char5(size), "6": Char6(size), "7": Char7(size), "8": Char8(size), "9": Char9(size)}
    for number in x:
        for key in numDict:
            if (key == number):
                numDict[key].draw(posX, posY)
                posX += size * 1.25

t.mainloop()
