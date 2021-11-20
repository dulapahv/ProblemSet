from turtle import *

def calendar_of_2021(month):
    speed(0)
    pu()
    setpos(-125, 100)
    pd()
    monthTxt = ["January", "February", "March", "April", "May", "June", "July", 'August', "September", "October", "November", "December"]
    dateTxt = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    dateRange = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dateStart = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
    for i in range(2):
        fd(250)
        rt(90)
        fd(30)
        rt(90)
    rt(90)
    fd(30)
    lt(90)
    fd(125)
    write(f"{monthTxt[month - 1]} 2021", font = ("Arial", 14), align = "center")
    fd(-125)

    for i in range(7):
        for j in range(2):
            fd(250 / 7)
            rt(90)
            fd(30)
            rt(90)
        fd(250 / 7)
    fd(-250)
    rt(90)
    fd(30)
    lt(90)
    pu()
    for i in range(7):
        write(f"  {dateTxt[i]}", font = ("Arial", 12))
        fd(250 / 7)
    fd(-250)
    pendown()
    
    datePos = dateStart[month - 1]
    dateCount = (0 - datePos) + 1
    while dateCount <= dateRange[month - 1]:
        for i in range(7):
            if 1 <= dateCount <= dateRange[month - 1]:
                rt(90)
                fd(30)
                lt(90)
                write(f"   {dateCount}", font = ("Arial", 12))
                lt(90)
                fd(30)
                rt(90)
            for j in range(2):
                fd(250 / 7)
                rt(90)
                fd(30)
                rt(90)
            fd(250 / 7)
            dateCount += 1
            datePos += 1
        rt(90)
        fd(30)
        lt(90)
        fd(-250)    
    hideturtle()
    done()