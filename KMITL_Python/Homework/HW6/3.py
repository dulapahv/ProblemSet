from turtle import *

def draw_rectangle(size): 
    color("#00247d")
    begin_fill()
    for i in range(2):
        fd(size * 6) 
        left(90)
        fd(size * 3) 
        left(90)
    end_fill()

def draw_redcross(size):
    pu()
    home()
    pd()
    color("#cf142b")
    draw_parallelogram1(size)
    pu()
    setheading(0)
    fd(size * 6)
    pd()
    draw_parallelogram2(size)
    pu()
    setheading(0)
    left(90)
    fd(size * 3)
    pd()
    setheading(180)
    draw_parallelogram1(size)
    pu()
    setheading(180)
    fd(size * 6)
    pd()
    draw_parallelogram2(size)

def draw_whitecross(size):
    x = 0.4
    y = 0.8
    a = 2.45978
    b = 2.45925
    color("white")
    begin_fill()
    for i in range(2):
        fd(size * y) 
        left(26.57)
        fd(size * a)
        right(53.14)
        fd(size * a)
        if i != 1:
            setheading(0)
        else:
            setheading(180)
        fd(size * y) 
        left(90) 
        fd(size * x)
        left(63.43)
        fd(size * b)
        right(126.86)
        fd(size * b)
        if i != 1:
            setheading(0)
        else:
            setheading(180)
        left(90)
        fd(size * x) 
        left(90)
    end_fill()

def draw_parallelogram1(size):
    begin_fill()
    left(26.57)
    for i in range(2):
        fd(size * 2.6)
        right(26.57)
        fd(size * 0.45)
        right(153.43)
    setheading(0)
    end_fill()

def draw_parallelogram2(size):
    begin_fill()
    left(153.43)
    for i in range(2):
        fd(size * 2.6)
        right(63.43)
        fd(size * 0.23)
        right(116.57)
    setheading(0)
    end_fill()

def draw_whiteplus(size):
    pu()
    home()
    fd(size * 2.5)
    left(90)
    pd()
    draw_whiteplus1(size)
    pu()
    left(90)
    fd(size)
    setheading(0)
    pd()
    draw_whiteplus2(size)

def draw_whiteplus1(size):
    color('white')
    begin_fill()
    for i in range(2):
        fd(size * 3)
        right(90)
        fd(size)
        right(90)
    end_fill()
    pu()
    home()
    pd()

def draw_whiteplus2(size):
    color("white")
    begin_fill()
    for i in range(2):
        fd(size * 6)
        left(90)
        fd(size)
        left(90)
    end_fill()
    pu()
    home()
    pd()

def draw_redplus(size):
    pu()
    home()
    fd(size * 2.7)
    left(90)
    pd()
    draw_redplus1(size)
    pu()
    left(90)
    fd(size * 1.2)
    setheading(0)
    pd()
    draw_redplus2(size)

def draw_redplus1(size):
    color("#cf142b")
    begin_fill()
    for i in range(2):
        fd(size * 3)
        right(90)
        fd(size * 0.6)
        right(90)
    end_fill()
    pu()
    home()
    pd()

def draw_redplus2(size):
    color('#cf142b')
    begin_fill()
    for i in range(2):
        fd(size * 6)
        left(90)
        fd(size * 0.6)
        left(90)
    end_fill()
    pu()
    home()
    pd()

def draw_polygon(size):
    draw_whitecross(size)
    draw_redcross(size)
    draw_whiteplus(size)
    draw_redplus(size)

def uk_flag(size = 100):
    speed(0)
    draw_rectangle(size)
    draw_polygon(size)
    hideturtle()
    done()