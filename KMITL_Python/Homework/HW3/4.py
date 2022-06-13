import turtle

t = turtle.Turtle()
t.penup()
t.setpos(-220, 0)
r = float(input("Radius: "))
t.pen(pensize = 10 * (r / 100), speed = 0)

def drawCircle(color, r, i):
    x, y = 110 * (r / 100), 100 * (r / 100)
    t.pencolor(color)
    t.pendown()
    t.circle(r)
    t.penup()
    t.fd(x)
    t.lt(90)
    t.fd(y * i)
    t.rt(90)


drawCircle("#0085C7", r, -1)
drawCircle("#F4C300", r, 1)
drawCircle("#000000", r, -1)
drawCircle("#009F3D", r, 1)
drawCircle("#DF0024", r, -1)

t.hideturtle()
turtle.done()