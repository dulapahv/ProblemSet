import turtle

t = turtle.Turtle()
n = int(input("Enter number of N: "))

t.pen(speed=0, fillcolor="grey")
for i in range(n):
	for j in range(n):
		if (i + j) % 2 == 0:
			t.begin_fill()
		for k in range(4):
			t.fd(100 / n)
			t.rt(90)
		t.fd(100 / n)
		t.end_fill()
	t.rt(90)
	t.fd(100 / n)
	t.rt(90)
	t.fd(100)
	t.rt(180)
t.ht()

turtle.done()
