class Calculator:
    def __init__(self, acc = 0):
        self.acc = acc
    
    def set_accumulators(self, a):
        self.acc = a
    
    def get_accumulators(self):
        return self.acc
    
    def add(self, x):
        self.acc += x
    
    def subtract(self, x):
        self.acc -= x
    
    def multiply(self, x):
        self.acc *= x
    
    def divide(self, x):
        self.acc /= x
    
    def print_results(self):
        print(f"Result: {self.acc}")
    

class Sci_Calc(Calculator):
    def __init__(self, acc):
        super().__init__(acc)
    
    def exp(self, x):
        self.acc **= x
    
    def factorial(self):
        if self.acc == 0 or self.acc == 1:
            self.acc = 1
            return self.acc
        self.fact = 1
        for i in range(1, self.acc + 1):
            self.fact = self.fact * i
        self.acc = self.fact
        return self.acc
    
    def print_results(self):
        print(f"Result: {self.acc:e}")
