import turtle
turtle.speed(1)
if leo.x < 0:
    turtle.backward(abs(leo.x))
else:
    turtle.forward(leo.x)

if leo.y < 0:
    turtle.right(90)
    turtle.forward(abs(leo.y))
else:
    turtle.left(90)
    turtle.forward(leo.y)

turtle.done()