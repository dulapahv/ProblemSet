import turtle

t = turtle.Turtle()
t.speed(0)
l = float(input("Length: "))

t.lt(72)
for i in range(5):
    t.fd(l)
    t.rt(144)

t.hideturtle()
turtle.done()