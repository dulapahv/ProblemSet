import turtle
import math

def Calc_Distance(x2, x1, y2, y1):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def Is_Point_In_Rect(aX, wX, aY, wY, bX, bY):
    return (0 < Calc_Distance(aX, wX, aY, wY) * Calc_Distance(aX, bX, aY, bY) < Calc_Distance(aX, bX, aY, bY) * Calc_Distance(aX, bX, aY, bY)) and (
            0 < Calc_Distance(aX, wX, aY, wY) * Calc_Distance(aX, dX, aY, dY) < Calc_Distance(aX, dX, aY, dY) * Calc_Distance(aX, dX, aY, dY))

t = turtle.Turtle()

t.pen(pensize = 1, speed = 0)
t.hideturtle()
t.setpos(0, -1000)
t.setpos(0, 1000)
t.penup()
t.setpos(-1000,0)
t.pendown()
t.setpos(1000, 0)

t.pensize(2)
r1x, r1y = input("Enter x,y coordinate for rectangle 1: ").split(",")
r1w = float(input("Enter width for rectangle 1: "))
r1h = float(input("Enter height for rectangle 1: "))
t.penup()
t.setpos(float(r1x) * 10, float(r1y) * 10)
t.write(f"R1 ({r1x}, {r1y})", font=("Arial", 14))
t.setpos((float(r1x) - (float(r1w) / 2)) * 10, (float(r1y) + (float(r1h) / 2)) * 10)
t.pendown()
for i in range(2):
    t.fd(float(r1w) * 10)
    t.rt(90)
    t.fd(float(r1h) * 10)
    t.rt(90)

r2x, r2y = input("Enter x,y coordinate for rectangle 2: ").split(",")
r2w = float(input("Enter width for rectangle 2: "))
r2h = float(input("Enter height for rectangle 2: "))
t.penup()
t.setpos(float(r2x) * 10, float(r2y) * 10)
t.write(f"R2 ({r2x}, {r2y})", font=("Arial", 14))
t.setpos((float(r2x) - (float(r2w) / 2)) * 10, (float(r2y) + (float(r2h) / 2)) * 10)
t.pendown()
for i in range(2):
    t.fd(float(r2w) * 10)
    t.rt(90)
    t.fd(float(r2h) * 10)
    t.rt(90)

aX, aY = ((float(r1x) - (float(r1w) / 2)) * 10, (float(r1y) + (float(r1h) / 2)) * 10) # A
bX, bY = ((float(r1x) + (float(r1w) / 2)) * 10, (float(r1y) + (float(r1h) / 2)) * 10) # B
cX, cY = ((float(r1x) - (float(r1w) / 2)) * 10, (float(r1y) - (float(r1h) / 2)) * 10) # C
dX, dY = ((float(r1x) + (float(r1w) / 2)) * 10, (float(r1y) - (float(r1h) / 2)) * 10) # D
wX, wY = ((float(r2x) - (float(r2w) / 2)) * 10, (float(r2y) + (float(r2h) / 2)) * 10) # W
xX, xY = ((float(r2x) + (float(r2w) / 2)) * 10, (float(r2y) + (float(r2h) / 2)) * 10) # X
yX, yY = ((float(r2x) - (float(r2w) / 2)) * 10, (float(r2y) - (float(r2h) / 2)) * 10) # Y
zX, zY = ((float(r2x) + (float(r2w) / 2)) * 10, (float(r2y) - (float(r2h) / 2)) * 10) # Z

checkA = Is_Point_In_Rect(aX, wX, aY, wY, bX, bY)
checkB = Is_Point_In_Rect(aX, xX, aY, xY, bX, bY)
checkC = Is_Point_In_Rect(aX, yX, aY, yY, bX, bY)
checkD = Is_Point_In_Rect(aX, zX, aY, zY, bX, bY)
checkW = Is_Point_In_Rect(wX, aX, wY, aY, xX, xY)
checkX = Is_Point_In_Rect(wX, bX, wY, bY, xX, xY)
checkY = Is_Point_In_Rect(wX, cX, wY, cY, xX, xY)
checkZ = Is_Point_In_Rect(wX, abs(dX), wY, abs(dY), xX, xY)

if checkA and checkB and checkC and checkD:
    print("Rectangle 2 is inside Rectangle 1.")
elif checkW and checkX and checkY and checkZ:
    print("Rectangle 1 is inside Rectangle 2.")
elif checkA or checkB or checkC or checkD or checkW or checkX or checkY or checkZ:
    print("Rectangle 1 overlaps Rectangle 2.")
else:
    print("Neither Rectangle 1 nor Rectangle 2 overlaps.")

turtle.done()