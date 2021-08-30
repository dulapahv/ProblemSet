import turtle
import math

t = turtle.Turtle()

t.pen(pensize = 1, speed = 0)
t.setpos(0, -1000)
t.setpos(0, 1000)
t.penup()
t.setpos(-1000,0)
t.pendown()
t.setpos(1000, 0)
t.penup()

t.pensize(2)
p0x, p0y = (input("Enter x,y coordinate for P0: ")).split(",")
t.setpos(float(p0x) * 10, float(p0y) * 10)
t.pendown()
t.write(f"P0 ({p0x}, {p0y})", font=("Arial", 14))
p1x, p1y = (input("Enter x,y coordinate for P1: ")).split(",")
t.setpos(float(p1x) * 10, float(p1y) * 10)
t.write(f"P1 ({p1x}, {p1y})", font=("Arial", 14))

t.shapesize(1.5)
angle = math.degrees(math.atan((float(p1y) - float(p0y)) / (float(p1x) - float(p0x))))
if float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0:
    t.lt(angle + 180)
elif float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0:
    t.lt(angle + 180)
else:
    t.lt(angle)
t.clone()
t.penup()
t.hideturtle()

p2x, p2y = (input("Enter x,y coordinate for P2: ")).split(",")
t.setpos(float(p2x) * 10, float(p2y) * 10)
t.dot(10)

if float(p0x) <= float(p1x):
    xLim1 = float(p0x)
    xLim2 = float(p1x)
else:
    xLim1 = float(p1x)
    xLim2 = float(p0x)

if float(p0y) <= float(p1y):
    yLim1 = float(p1y)
    yLim2 = float(p0y)
else:
    yLim1 = float(p0y)
    yLim2 = float(p1y)

m = (float(p1y) - float(p0y)) / (float(p1x) - float(p0x))
if (float(p2y) - float(p0y)) == m * ((float(p2x) - float(p0x))) and float(p2x) >= xLim1 and float(p2y) <= yLim1 and float(p2x) <= xLim2 and float(p2y) >= yLim2:
    msg = "P2 is on the line between P0 and P1."
elif (float(p2y) - float(p0y)) > m * ((float(p2x) - float(p0x))) and float(p2x) >= xLim1 and float(p2y) <= yLim1 and float(p2x) <= xLim2 and float(p2y) >= yLim2:
    if float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0:
        msg = "P2 is on the right side of the line between P0 and P1."
    elif float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0:
        msg = "P2 is on the right side of the line between P0 and P1."
    else:
        msg = "P2 is on the left side of the line between P0 and P1."
elif (float(p2y) - float(p0y)) < m * ((float(p2x) - float(p0x))) and float(p2x) >= xLim1 and float(p2y) <= yLim1 and float(p2x) <= xLim2 and float(p2y) >= yLim2:
    if float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0:
        msg = "P2 is on the left side of the line between P0 and P1."
    elif float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0:
        msg = "P2 is on the left side of the line between P0 and P1."
    else:
        msg = "P2 is on the right side of the line between P0 and P1."
else:
    msg = "P2 is neither on the line nor located between P0 and P1."

t.write(f"P2 ({p2x}, {p2y})\n{msg}", font=("Arial", 14))
print(msg)
turtle.done()