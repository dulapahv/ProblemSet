import random

width = int(input("Rectangle width: "))
height = int(input("Rectangle height: "))
border = int(input("Border thickness: "))

for i in range(height):
	for j in range(width):
		# top and bottom border
		if height - border <= i <= height or 0 <= i <= border - 1:
			print(random.choice(["#", "*", "$"]), end="")
		# left and right border
		elif 0 <= j <= border - 1 or width - border <= j <= width:
			print(random.choice(["#", "*", "$"]), end="")
		else:
			print(" ", end="")
	print()
