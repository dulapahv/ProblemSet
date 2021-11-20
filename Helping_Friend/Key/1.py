from math import pi


def circle_area(r):
    area = pi * (r**2)
    return area


def circle_circumference(r):
    circumference = 2 * pi * r
    return circumference

r = float(input("Enter circle radius: "))
print(f"Circle's circumference is {circle_area(r):.2f}")
print(f"The area of circle is {circle_circumference(r):.2f}")