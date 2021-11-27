def permute(t):
    tempList = list(t)
    if len(tempList) == 1:
        newList = [tempList]
    else:
        newList = []
        for index in range(len(tempList)):
            all_value = permute(tempList[0:index] + tempList[index + 1:])
            for value in all_value:
                newList.append(tempList[index:index+1] + value)
    return newList

def perm3(t):
    permList = permute(t)
    for index in range(len(permList)):
        print(tuple(permList[index][0:len(permList[index]) - (len(permList[index]) - 3)]), end = " ")

perm3((1,2,3,4))
