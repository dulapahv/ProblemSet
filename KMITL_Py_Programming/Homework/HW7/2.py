class Poly:
    def __init__(self, p):
        self.p = list(p)
    
    def add(self, p2):
        for i in range(len(self.p)):
            self.p[i] += p2[i]
        return Poly(tuple(self.p))
    
    def eval(self, num):
        ans = 0
        for i in range(len(self.p)):
            ans += (self.p[i] * (num**i))
        return ans
    
    def scalar_multiply(self, num):
        for i in range(len(self.p)):
            self.p[i] *= num
        return Poly(tuple(self.p))

    def multiply(self, p2):
        ans = [0] * (len(self.p) + len(p2) - 1)
        for i in range(len(self.p)):
            for j in range(len(p2)):
                ans[i + j] += self.p[i] * p2[j]
        self.p = ans
        return tuple(self.p)
    
    def power(self, num):
        for i in range(num - 1):
            list(self.p) = self.multiply(list(self.p))
        return Poly(tuple(self.p))
    
    def diff(self):
        for i in range(len(self.p) - 1):
            self.p[i] = self.p[i + 1] * (i + 1)
        self.p.pop(-1)
        return Poly(tuple(self.p))

    def integrate(self):
        self.p.append(0)
        for i in range(len(self.p) - 1, 0, -1):
            self.p[i] = self.p[i - 1] / i
        self.p[0] = 0
        return Poly(tuple(self.p))
    
    def print(self):
        for i in range(len(self.p)):
            if self.p[i] != 0:
                if i == 0:
                    if self.p[i] > 0 and self.p[i] != 0:
                        print(self.p[i], end = " ")
                        print("+", end = " ")
                    else:
                        print(self.p[i], end = " ")
                elif i == 1:
                    if self.p[i] > 0 and self.p[i] != 0:
                        print(self.p[i], "x", sep = "", end = " ")
                elif i < len(self.p) - 1:
                    if self.p[i] > 0 and self.p[i] != 0:
                        print("+", end = " ")
                        print(self.p[i], "x^", i, sep = "", end = " ")
                else:
                    if self.p[i] > 0 and self.p[i] != 0:
                        print("+", end = " ")
                        print(self.p[i], "x^", i, sep = "", end = " ")