import math as m

a = float(input())
b = float(input())
c = float(input())

root1 = round((-b - m.sqrt((b**2) - (4*a*c))) / (2*a), 3)
root2 = round((-b + m.sqrt((b**2) - (4*a*c))) / (2*a), 3)

print(f'{root1} {root2}')
