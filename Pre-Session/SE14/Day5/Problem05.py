import turtle

t = turtle.Turtle()


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
	colorList = ["red", "orange", "yellow",
				 "green", "blue", "indigo", "violet"]
	t.speed(0)
	t.sety(-100)
	for i in range(len(occurrencesList)):
		t.fillcolor(colorList[i])
		t.begin_fill()
		t.circle(100, occurrencesList[i] * 360 / sum(occurrencesList))
		pos = t.pos()
		t.setpos(0, 0)
		t.end_fill()
		t.setpos(pos)
	t.ht()
	turtle.mainloop()


exec(input())
