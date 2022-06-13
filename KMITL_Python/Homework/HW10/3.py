def my_union(numList1, numList2):
    newList = []
    for i in range(len(numList1)):
        if numList1[i] not in newList:
            newList.append(numList1[i])
    for i in range(len(numList2)):
        if numList2[i] not in newList:
            newList.append(numList2[i])
    return newList

def my_intersection(numList1, numList2):
    newList = []
    for i in range(len(numList1)):
        if numList1[i] in numList2:
            if numList1[i] not in newList:
                newList.append(numList1[i])
    for i in range(len(numList2)):
        if numList2[i] in numList1:
            if numList2[i] not in newList:
                newList.append(numList2)
    return newList

def my_difference(numList1, numList2):
    newList = []
    for i in range(len(numList1)):
        chk = 0
        for j in range(len(numList2)):
            if numList1[i] == numList2[j]:
                chk = 1
        if chk == 0:
             newList.append(numList1[i])
    return newList