class Poly:
    #Initialization (tuple x)
    def __init__(self, x):
        self.x = list(x)
    
    #ADDITION Method
    def add(self, poly):
        for i in range(len(self.x)):
            self.x[i] += poly[i]
        return self.x

    #SCALAR MULTIPLICATION Method
    def scalar_multiply(self, c):
        for i in range(len(self.x)):
            self.x[i] *= c
        return self.x

    #POLYNOMIALS MULTIPLICATION Method
    def multiply(self, poly): # input (1, 2, 3) * (4, 5, 6)
        ans = [0] * (len(self.x) + len(poly) - 1) # Create a 0-filled array to store answer. The array size is the sum of length of 2 poly object - 1
        for i in range(len(self.x)): # Loop through each polynomial in the first array
            for j in range(len(poly)): # Loop through each polynomial in the second array
                ans[i + j] += self.x[i] * poly[j] # Multiply coefficient. And also determine the position of the polynomial.
        return ans
    #self.x[i] = self.x's coefficient, poly[j] = poly's coefficient

    #POWER Method
    def power(self, n):
        ans = self.x
        for i in range(n):
            ans = self.multiply(self.x)
        return ans

    #DIFF Method
    def diff(self):
        ans = [0] * (len(self.x))
        term = len(self.x) - 1
        for i in range(term):
            ans[i] = self.x[i + 1] * (i + 1)
        ans.pop(-1) # remove the last element from array
        return ans

    #INTEGRATE Method
    def integrate(self):
        ans = [0] * (len(self.x) + 1)
        term = len(self.x) 
        for i in range(term):
            ans[i + 1] = self.x[i] / (i + 1)
            print(ans[i + 1])
        ans[0] = 0
        return ans

    #EVALUATE Method
    def evaluate(self, n):
        ans = 0
        term = len(self.x)
        for i in range(term):
            ans += self.x[i] * (n ** i)
        return ans

    #OUTPUT (Print) METHOD
    def prntpoly(self):
        
        for i in range(len(self.x)):
            
            if self.x[i] >= 0: #General sign
                sign = "+"
            else:
                sign = "-"
            
            if i == 0: #First term without x
                if sign == "+":
                    sign = ""
                print(f"{sign}{self.x[i]} ", end = "")
            
            else: #2nd+ term
                if self.x[i] != 0: #Non-zero coefficient
                    if i == 1: #Second non-zero term (x only)
                        print(f"{sign} {self.x[i]}x ", end = "")
                    elif self.x[i] == 1:
                        print(f"{sign} x^{i} ", end = "")
                    else:
                        print(f"{sign} {self.x[i]}x^{i} ", end = "")
                else:
                    print("")

p = Poly((1,7,5,1))
# print(p.multiply((3,4,5))) # [6, 23, 66, 91, 84, 30] --> 6 + 23x + 66x^2 + 91x^3 + 84x^4 + 30x^5
# print(p.power(2))
# print(p.integrate())
# print(p.evaluate(2))
p.prntpoly()