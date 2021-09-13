import turtle

t = turtle.Turtle()

t.speed(0)

x = int(input("Enter x: "))

def draw_square(x):
   for i in range(4):
       t.fd(x)
       t.lt(90)

def draw_pattern(x):
   for i in range(4):
       for j in range(5):
           draw_square(x * j)
       t.rt(90)

draw_pattern(x)

turtle.done()