import numpy as np

m,r = [],[]
for i in range(4):
    tmp=[]
    for j in range(4):
        tmp.append(j+i)
    m.append(tmp)

n = np.array(m)
row,col = n.shape
for i in range(row):
    tmp=[]
    for j in range(col):
        tmp.append(n[i,j])
    r = r + tmp
print(sum(r))