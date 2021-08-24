import turtle

t = turtle.Turtle()
t.pen(speed = 0)
t.setpos(0, -1000)
t.setpos(0, 1000)
t.penup()
t.setpos(-1000,0)
t.pendown()
t.setpos(1000, 0)
t.penup()

p1x, p1y = input("Enter x,y coordinate for P1: ").split(",")
t.setpos(float(p1x) * 10, float(p1y) * 10)
t.write(f"p1 ({p1x}, {p1y})", font=("Arial", 16, "normal"))
t.pensize(2)
t.pendown()
p2x, p2y = input("Enter x,y coordinate for P2: ").split(",")
t.setpos(float(p2x) * 10, float(p2y) * 10)
t.write(f"p2 ({p2x}, {p2y})", font=("Arial", 16, "normal"))
p3x, p3y = input("Enter x,y coordinate for P3: ").split(",")
t.setpos(float(p3x) * 10, float(p3y) * 10)
t.write(f"p3 ({p3x}, {p3y})", font=("Arial", 16, "normal"))
t.setpos(float(p1x) * 10, float(p1y) * 10)
t.penup()

area = abs((0.5) * (float(p1x) * (float(p2y) - float(p3y)) + 
                    float(p2x) * (float(p3y) - float(p1y)) + 
                    float(p3x) * (float(p1y) - float(p2y))))

t.setpos(0, 0)
t.color("red")
t.write(f"Area = {area:.2f}", font=("Arial", 16, "bold"))
print(f"The area of a triangle is {area:.2f}")

t.hideturtle()
turtle.done()