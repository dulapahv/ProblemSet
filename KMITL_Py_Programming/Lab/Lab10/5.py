def my_sort(numList):
    L = []
    L.append(numList[0])
    for i in range(1, len(numList)):
        for j in range(len(L)):
            if numList[i] < L[j]:
                L.insert(j, numList[i])
                break
    return L

print(my_sort([6, 4, 2, 1, 4]))