def my_count(numList):
    count = 0
    for i in range(len(numList)):
        if numList[i] >= 0:
            count += 1
    return count

print(my_count([-3,2,0,1,-5,5,6]))