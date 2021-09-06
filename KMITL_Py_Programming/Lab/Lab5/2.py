import turtle

t = turtle.Turtle()
n = int(input("Enter number of N: "))

t.speed(0)
for i in range(4):
    t.fd(100)
    t.rt(90)

for i in range(n):
    for j in range(n):
        for k in range(4):
            t.fd(100 / n)
            t.rt(90)
        t.fd(100 / n)
    t.rt(90)
    t.fd(100 / n)
    t.rt(90)
    t.fd(100)
    t.rt(180)

turtle.done()