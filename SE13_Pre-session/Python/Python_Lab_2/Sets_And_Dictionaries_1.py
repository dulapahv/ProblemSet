def Merge(FirstDict, SecondDict):
    result = FirstDict.copy()
    result.update(SecondDict)
    return result

Dict1 = {'A': 10, 'B': 20}
Dict2 = {'C': 30, 'D': 40}

print(Merge(Dict1, Dict2))
print(Dict2)
