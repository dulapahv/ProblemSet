import turtle

t = turtle.Turtle()

def draw_polygon(x, y, side = 4, size = 100):
    for i in range(side):
        t.fd(size)
        t.rt(360 / side)

draw_polygon(10, 10, 5, 200)
turtle.done()