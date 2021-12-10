L1 = [5,1,2,8,9,12,16]
L2 = [2*x for x in L1 if x%2 == 0]
L3 = [y//2 for y in L2 if y%2 == 0 and y!= 1]
print(sum(L3))