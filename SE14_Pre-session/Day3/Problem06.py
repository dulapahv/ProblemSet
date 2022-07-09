myList = input()[1:-1].replace(' ', '').split(',')
try:
	myList = [int(num) for num in myList]
except ValueError:
	print('Error')
	exit()
for i in range(len(myList)):
	for j in range(i + 1, len(myList)):
		if myList[i] > myList[j]:
			myList[i], myList[j] = myList[j], myList[i]

print(myList)
