from turtle import *

def histogram(numList):
    numberList = []
    occurrencesList = []
    num = 1
    for i in range(len(numList)):
        count = 0
        for j in range(len(numList)):
            if numList[j] == num:
                count += 1
        if count != 0:
            numberList.append(num)
            occurrencesList.append(count)
        num += 1
    speed(0)
    fd(50)
    for i in range(len(numberList)):
        pd()
        fd(50)
        pu()
        rt(90)
        fd(30)
        rt(90)
        fd(50)
        write(f"{i + 1}", font=("Arial", 16, "bold"))
        rt(90)
        fd(30)
        rt(90)
        fd(50)
    pd()
    write(f"X", font=("Arial", 16, "bold"))
    setpos(0, 0)
    lt(90)
    fd(300)
    write(f"Y", font=("Arial", 16, "bold"))
    pen(fillcolor = "purple")
    pu()
    for i in range(len(numberList)):
        setpos(50 * (i + 1) - 20, 0)
        begin_fill()
        for j in range(2):
            fd(30 * occurrencesList[i])
            rt(90)
            fd(50)
            rt(90)
        end_fill()
    hideturtle()
    done()

histogram( [1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4,4] )
