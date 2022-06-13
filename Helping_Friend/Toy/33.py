def printMat(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            s = f'{m[i][j]:2}'
            print(s, end='')
        print()

def T(m):
    for i in range(len(m)):
        for j in range(i, len(m[i])):
            tmp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = tmp
    return m

m = []
for i in range(4):
    tmp = []
    for j in range(4):
        tmp.append(j+i*2)
    m.append(tmp)

printMat(T(m))