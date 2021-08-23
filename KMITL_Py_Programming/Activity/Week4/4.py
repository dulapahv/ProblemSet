import turtle

t = turtle.Turtle()
t.penup()
t.setpos(-220, 0)
t.pen(pensize = 10, speed = 0)


def drawCircle(color, i):
    r, x, y = 100, 110, 100
    t.pencolor(color)
    t.pendown()
    t.circle(r)
    t.penup()
    t.fd(x)
    t.lt(90)
    t.fd(y * i)
    t.rt(90)


drawCircle("#0085C7", -1)
drawCircle("#F4C300", 1)
drawCircle("#000000", -1)
drawCircle("#009F3D", 1)
drawCircle("#DF0024", -1)

t.hideturtle()
turtle.done()