import turtle

t = turtle.Turtle()
t.speed(0)

size = int(input('Size: '))
height = size / 6
width = size * 1.5

t.fillcolor("red")
t.begin_fill()
for i in range(2):
	for i in range(2):
		t.pd()
		t.fd(width)
		t.rt(90)
		t.fd(height)
		t.rt(90)
	t.pu()
	t.rt(90)
	t.fd(height * 5)
	t.lt(90)
t.end_fill()

t.lt(90)
t.fd(height * 9)
t.rt(90)

t.fillcolor('white')
t.begin_fill()
for i in range(2):
	for i in range(2):
		t.pd()
		t.fd(width)
		t.rt(90)
		t.fd(height)
		t.rt(90)
	t.pu()
	t.rt(90)
	t.fd(height * 3)
	t.lt(90)
t.end_fill()

t.lt(90)
t.fd(height * 5)
t.rt(90)

t.fillcolor('#130AC8')
t.begin_fill()
t.pd()
for i in range(2):
	for i in range(2):
		t.fd(width)
		t.rt(90)
		t.fd(height * 2)
		t.rt(90)
t.end_fill()
t.ht()

turtle.done()
