import math as m

n = int(input())

lower = (m.sqrt(2*m.pi)) * (n**(n+(1/2))) * (m.e**(-n + (1/((12*n)+1))))
upper = (m.sqrt(2*m.pi)) * (n**(n+(1/2))) * (m.e**(-n + (1/(12*n))))

print(lower)
print(upper)
