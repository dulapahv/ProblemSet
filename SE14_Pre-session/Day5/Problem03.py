import turtle

t = turtle.Turtle()


def calendar_of_2022(month):
    t.speed(0)
    t.pu()
    t.setpos(-125, 100)
    t.pd()
    monthTxt = ["January", "February", "March", "April", "May", "June",
                "July", 'August', "September", "October", "November", "December"]
    dateTxt = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    dateRange = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dateStart = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
    for i in range(2):
        t.fd(250)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.fd(125)
    t.write(f"{monthTxt[month - 1]} 2022", font=("Arial", 14), align="center")
    t.fd(-125)

    for i in range(7):
        for j in range(2):
            t.fd(250 / 7)
            t.rt(90)
            t.fd(30)
            t.rt(90)
        t.fd(250 / 7)
    t.fd(-250)
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.pu()
    for i in range(7):
        t.write(f"  {dateTxt[i]}", font=("Arial", 12))
        t.fd(250 / 7)
    t.fd(-250)
    t.pd()

    datePos = dateStart[month - 1]
    dateCount = (0 - datePos) + 1
    while dateCount <= dateRange[month - 1]:
        for i in range(7):
            if 1 <= dateCount <= dateRange[month - 1]:
                t.rt(90)
                t.fd(30)
                t.lt(90)
                t.write(f"   {dateCount}", font=("Arial", 12))
                t.lt(90)
                t.fd(30)
                t.rt(90)
            for j in range(2):
                t.fd(250 / 7)
                t.rt(90)
                t.fd(30)
                t.rt(90)
            t.fd(250 / 7)
            dateCount += 1
            datePos += 1
        t.rt(90)
        t.fd(30)
        t.lt(90)
        t.fd(-250)
    t.ht()
    turtle.done()


calendar_of_2022(9)
