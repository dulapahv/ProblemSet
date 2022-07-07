code = input()

A = code[3] + code[10] + code[17] + code[24] + code[31]
B = code[7] + code[12] + code[17] + code[22] + code[27]
C = str(int(A) + int(B) + 10000)
D = C[-4] + C[-3] + C[-2]
E1 = int(D[0]) + int(D[1]) + int(D[2])
E2 = (E1 % 10) + 1

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
F = letters[E2 - 1]
G = str(D) + F

print(G)
