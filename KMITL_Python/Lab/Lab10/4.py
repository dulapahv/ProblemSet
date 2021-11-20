def get_the_difference(numList1, numList2):
    newList = []
    for i in range(len(numList1)):
        chk = 0
        for j in range(len(numList2)):
            if numList1[i] == numList2[j]:
                chk = 1
        if chk == 0:
             newList.append(numList1[i])

    for i in range(len(numList2)):
        chk = 0
        for j in range(len(numList1)):
             if numList2[i] == numList1[j]:
                 chk = 1
        if chk == 0:
            newList.append(numList2[i])
    return newList

print(get_the_difference([3,1,1,1,2,7],[4,1,1,2,2,5]))