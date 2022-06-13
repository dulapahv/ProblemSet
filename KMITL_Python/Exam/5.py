from turtle import *

def draw_nested_squares(size, gap):
    for i in range(4):
        length = int(size / (size / (gap * 2)) / 2)
        for j in range(int(size / (gap * 2))):
            pu()
            fd(length)
            lt(90)
            pd()
            fd(length)
            lt(90)
            fd(length)
            lt(90)
            pu()
            fd(length)
            lt(90)
            length += gap
        rt(90)
    
draw_nested_squares(200, 20)
mainloop()