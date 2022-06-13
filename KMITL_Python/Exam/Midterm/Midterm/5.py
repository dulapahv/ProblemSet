from turtle import *
speed(8)
def draw_sq(n):
    for i in range(4):
        fd(n)
        lt(90)

def spiral_sq(s):
    draw_sq(s)
    pu()
    fd(30)
    lt(90)
    fd(10)
    rt(90)
    pd()
    while s > 5:
        s *= 0.75
        lt(10)
        for i in range(4):
            fd(s)
            lt(90)
        pu()
        fd(30)
        lt(90)
        fd(5)
        rt(90)
        pd()
spiral_sq(150)
mainloop()