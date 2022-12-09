class LinearEquation:
    #Private initialization
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    #6 GET methods (a to f)
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

    #isSolvable method
    def isSolvable(self):
        if ((self.__a * self.__d) - (self.__b * self.__c)) != 0:
            return True
        else:
            return False

    #Solution methods
    def getX(self):
        n = (self.__e * self.__d) - (self.__b * self.__f)
        d = (self.__a * self.__d) - (self.__b * self.__c)
        return n / d
        
    def getY(self):
        n = (self.__a * self.__f) - (self.__e * self.__c)
        d = (self.__a * self.__d) - (self.__b * self.__c)
        return n / d