shift = int(input())
string = input()

for char in string:
	if char >= 'a' and char <= 'z':
		char = chr((((ord(char) - ord('a')) + shift) % 26) + ord('a'))
		print(char, end='')
	elif char >= 'A' and char <= 'Z':
		char = chr((((ord(char) - ord('A')) + shift) % 26) + ord('A'))
		print(char, end='')
	else:
		print(char, end='')
