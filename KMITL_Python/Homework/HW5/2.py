import turtle

t = turtle.Turtle()

turtle.tracer(0)
t.penup()
t.setpos(-525, 420)
t.pendown()
date = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
monthRow = [6, 5, 5, 5, 6, 5, 5, 5, 5, 6, 5, 5]
monthStart = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
monthEnd = [31, 24, 27, 29, 32, 27, 31, 26, 28, 31, 26, 29]
month = 0

# loop all month (column)
column = 0
while column < 3:
    # loop all month (row)
    row = 0
    while row < 4:
        # create month header
        datePos = -12
        dateNum = 1
        i = 0
        while i < 2:
            t.fd(245)
            t.rt(90)
            t.fd(25)
            t.rt(90)
            i += 1
        t.rt(90)
        t.fd(25) # 200 / 8
        t.lt(90)
        t.write(f"  Month#{month + 1}", font = ("Arial", 14))

        # create date header
        i = 0
        while i < 7:
            j = 0
            while j < 2:
                t.fd((200 // 7) + 7)
                t.rt(90)
                t.fd(25) # 200 / 8
                t.rt(90)
                j += 1
            t.fd((200 // 7) + 7)
            i += 1
        t.rt(90)
        t.fd(25) # 200 / 8
        t.rt(90)
        t.fd(245)
        t.rt(180)
        i = 0
        while i < 7:
            t.write(f" {date[i]}", font = ("Arial", 14))
            t.fd((200 // 7) + 7)
            i += 1
        t.rt(180)
        t.fd(245)
        t.rt(180)

        # create date
        i = 0
        while i <= monthRow[month]:
            j = 0
            while j < 7:
                k = 0
                while k < 2 and i < monthRow[month]:
                    t.fd((200 // 7) + 7)
                    t.rt(90)
                    t.fd(25) # 200 / 8
                    t.rt(90)
                    k += 1
                if i > 0 and monthStart[month] - 5 <= datePos < monthEnd[month]:
                    t.write(f" {dateNum}", font = ("Arial", 14))
                    dateNum += 1
                t.fd((200 // 7) + 7)
                j += 1
                datePos += 1
            if i < monthRow[month]:
                t.rt(90)
                t.fd(25) # 200 / 8
                t.rt(90)
                t.fd(245)
                t.rt(180)
            i += 1  
        t.penup()
        t.rt(90)
        t.fd(25) # 200 / 8
        t.rt(90)
        t.fd(245)
        t.rt(180)
        t.pendown()
        month += 1
        row += 1        
    t.penup()
    t.setpos(-525 + 400 * (column + 1), 420)
    t.pendown()
    column += 1
t.hideturtle()
turtle.update()
turtle.done()