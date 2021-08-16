import turtle
t = turtle.Turtle()
radius = float(input())
t.circle(radius)
t.hideturtle()
t.lt(90)
t.penup()
t.fd(radius)
area = 3.146 * radius * radius
t.write(area)
turtle.done()