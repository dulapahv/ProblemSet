L1 = [[5,1,2,8,9,12,16]]
m = list(L1[0])
a = [m[len(m)-i-1] for i in range(len(m))]
print(sum(L1[0]) + sum(a))