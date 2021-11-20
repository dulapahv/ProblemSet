def power(s):
    listS = list(s)
    subsets = []
    for i in range(2 ** len(listS)):
        subset = []
        for k in range(len(listS)):
            if i & 1 << k:
                subset.append(listS[k])
        subsets.append(subset)
    return subsets

s = set([1, 2, 3])
print(power(s))