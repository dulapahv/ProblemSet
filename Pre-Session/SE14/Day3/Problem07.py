row = int(input())
column = int(input())
M = []
for i in range(row):
	M.append(input().split(' '))

for i in range(row):
	for j in range(column):
		M[i][j] = int(M[i][j])

S = []
for i in range(row):
	temp = []
	for j in range(column):
		if i == 0 or j == 0:
			temp += M[i][j],
		else:
			temp += 0,
	S += temp,

for i in range(1, row):
	for j in range(1, column):
		if (M[i][j] == 1):
			S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
		else:
			S[i][j] = 0

max_of_s = S[0][0]
max_i = 0
max_j = 0
for i in range(row):
	for j in range(column):
		if (max_of_s < S[i][j]):
			max_of_s = S[i][j]
			max_i = i
			max_j = j

if max_i >= 2 or max_j >= 2:
	for i in range(row):
		for j in range(column):
			if (max_i - max_of_s < i <= max_i) and (max_j - max_of_s < j <= max_j):
				print('#', end=' ')
			else:
				print(M[i][j], end=' ')
		print()
else:
	print('None')
