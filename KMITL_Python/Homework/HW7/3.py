class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def isSolvable(self):
        if ((self.__a * self.__d) - (self.__b * self.__c)) != 0:
            return True
        else:
            return False

    def getX(self):
        if self.isSolvable() == True:
            x = ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
            return x
        else:
            return "Unsolvable"

    def getY(self):
        if self.isSolvable() == True:
            y = ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
            return y
        else:
            return "Unsolvable"