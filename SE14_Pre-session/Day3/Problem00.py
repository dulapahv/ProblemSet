height = int(input('Height: '))
for i in range(height):
	print(f'{" " * (height - i - 1)}{"#" * (i + 1)}')
