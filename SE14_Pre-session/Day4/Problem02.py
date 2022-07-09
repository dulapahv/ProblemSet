string = input().lower()

count = {}
for char in string:
	if char in count:
		count[char] += 1
	else:
		count[char] = 1

count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
keyList = [elem for elem in count.keys()]
valueList = [elem for elem in count.values()]

for i in range(len(keyList)):
	for j in range(i, len(valueList)):
		if valueList[i] == valueList[j]:
			if keyList[i] > keyList[j]:
				keyList[i], keyList[j] = keyList[j], keyList[i]

for i in range(len(keyList)):
	print(f'{keyList[i]} -> {valueList[i]}')
