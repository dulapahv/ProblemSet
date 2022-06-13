def merge(numList1, numList2):
    for i in numList1:
        for j in range(len(numList2)):
            if j != len(numList2) - 1:
                numList2.insert(j, i)
                break
            else:
                numList2.append(i)
    numList2.sort()
    return numList2

l1 = [1, 5, 16, 61, 111]
l2 = [2, 4, 5, 6]
print(merge(l1, l2))