p1x, p1y = input("Enter x,y coordinate for P1: ").split(",")
p2x, p2y = input("Enter x,y coordinate for P2: ").split(",")
p3x, p3y = input("Enter x,y coordinate for P3: ").split(",")

area = abs((0.5) * (float(p1x) * (float(p2y) - float(p3y)) + 
                    float(p2x) * (float(p3y) - float(p1y)) + 
                    float(p3x) * (float(p1y) - float(p2y))))
print(f"The area of a triangle is {area:.2f}")