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

# orient the arrow for reference direction to determine left/right
t.shapesize(1.5)
angle = math.degrees(math.atan((float(p1y) - float(p0y)) / (float(p1x) - float(p0x))))
if (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0) or (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0):
    t.lt(angle + 180)
else:
    t.lt(angle)
t.clone()
t.penup()
t.hideturtle()

t.pencolor("red")
p2x, p2y = (input("Enter x,y coordinate for P2: ")).split(",")
t.setpos(float(p2x) * 10, float(p2y) * 10)

m = (float(p1y) - float(p0y)) / (float(p1x) - float(p0x))
# check whether P2 lies between P0 and P1
if ((float(p2y) - float(p0y)) >= (-1 / m) * ((float(p2x) - float(p0x))) and (float(p2y) - float(p1y)) <= (-1 / m) * ((float(p2x) - float(p1x)))) or (
    ((float(p2y) - float(p0y)) <= (-1 / m) * ((float(p2x) - float(p0x))) and (float(p2y) - float(p1y)) >= (-1 / m) * ((float(p2x) - float(p1x))))):
    t.pencolor("green")
    # check whether P2 lies on the line between P0 and P1
    if (float(p2y) - float(p0y)) == m * ((float(p2x) - float(p0x))):
        msg = "P2 is on the line between P0 and P1."
    # determine the location of P2
    elif (float(p2y) - float(p0y)) > m * ((float(p2x) - float(p0x))) :
        if (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0) or (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0):
            msg = "P2 is on the right side of the line between P0 and P1."
        else:
            msg = "P2 is on the left side of the line between P0 and P1."
    elif (float(p2y) - float(p0y)) < m * ((float(p2x) - float(p0x))) :
        if (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) < 0) or (float(p1x) - float(p0x) < 0 and float(p1y) - float(p0y) > 0):
            msg = "P2 is on the left side of the line between P0 and P1."
        else:
            msg = "P2 is on the right side of the line between P0 and P1."
else:
    msg = "P2 is not either on the line or lies between P0 and P1."
t.dot(10)
t.write(f"P2 ({p2x}, {p2y})\n{msg}", font=("Arial", 14))
print(msg)
turtle.done()