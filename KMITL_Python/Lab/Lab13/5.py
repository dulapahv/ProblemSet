def subset(s):
    listS = list(s)
    subsets = []
    for i in range(2 ** len(listS)):
        subset = []
        for k in range(len(listS)):
            if i & 1 << k:
                subset.append(listS[k])
        subsets.append(subset)
    return subsets

def solve(list):
    ansList = []
    for subList in subset(list):
        if sum(subList) == 0:
            ansList.append(subList)
    return ansList[1:]

numList = [int(num) for num in input().split()]
if solve(numList):
    print(f"Yes, {solve(numList)}")
else:
    print("No")