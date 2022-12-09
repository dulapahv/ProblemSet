def inverse(dict):
    newDict = {}
    keyList = list(dict.keys())
    valueList = list(dict.values())
    for i in valueList:
        newSet = set()
        index = 0
        for j in valueList:
            if j == i:
                newSet.add(keyList[index])
            index += 1
        newDict[i] = newSet
    return(newDict)

dict = {'a':'1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
print(inverse(dict))