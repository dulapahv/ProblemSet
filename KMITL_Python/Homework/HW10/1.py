from turtle import *

def pie_chart(numList):
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
    colorList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    speed(0)
    sety(-100)
    for i in range(len(occurrencesList)):
        fillcolor(colorList[i])
        begin_fill()
        circle(100, occurrencesList[i] * 360 / sum(occurrencesList))
        pos = position()
        setpos(0, 0)
        end_fill()
        setpos(pos)
    hideturtle()
    mainloop()