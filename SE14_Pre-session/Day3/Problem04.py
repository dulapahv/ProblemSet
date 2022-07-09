nbr = input()

A = [str(int(num) * 2) for num in nbr[-2::-2]]
A = "".join(A)

chk = 0
for num in A:
	chk += int(num)

B = sum([int(num) for num in nbr[::-2]])
chk += B

start = int(nbr[0] + nbr[1])
length = len(nbr)
if (str(chk)[-1] == '0'):
	if (start == 34 or start == 37) and length == 15:
		print("AMEX")
	elif 51 <= start <= 55 and length == 16:
		print("MASTERCARD")
	elif nbr[0] == '4' and (length == 13 or length == 16):
		print("VISA")
	else:
		print("INVALID")
else:
	print("INVALID")
