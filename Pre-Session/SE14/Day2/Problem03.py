id = input()

a = int(id[0]) * 13
b = int(id[1]) * 12
c = int(id[2]) * 11
d = int(id[3]) * 10
e = int(id[4]) * 9
f = int(id[5]) * 8
g = int(id[6]) * 7
h = int(id[7]) * 6
i = int(id[8]) * 5
j = int(id[9]) * 4
k = int(id[10]) * 3
l = int(id[11]) * 2

chk = (11 - ((a + b + c + d + e + f + g + h + i + j + k + l) % 11)) % 10

g1 = id[0]
g2 = id[1] + id[2] + id[3] + id[4]
g3 = id[5] + id[6] + id[7] + id[8] + id[9]
g4 = id[10] + id[11]

print(f'{g1} {g2} {g3} {g4} {chk}')
