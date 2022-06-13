import turtle as t
t.speed(0)

def cross(size, spread):
    if spread >= 0:
        for i in range(4):
            t.fd(size)
            cross(size / 2, spread - 1) if spread != 1 else t.dot(5)          
            t.fd(size * -1)
            t.rt(90)
    else:
        t.dot(5)

cross(100, 4)
t.mainloop()
