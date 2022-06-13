from math import pi
x = float(input("What is the value of x? "))
y = float(input("What is the value of y? "))
d = float(input("What is the value of d? "))
print(f"Area of the lawn is {((x * y) - (pi * (d / 2)**2)):.2f} sq.m.")