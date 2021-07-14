def ToDictList(InputList):
    Dict = {'Name': None, 'Number': None}
    NewList = []
    for i in range(int(len(InputList) / 2)):
        Dict.update({'Name': InputList[i * 2]})
        Dict.update({'Number': InputList[(i * 2) + 1]})
        NewList.append(Dict.copy())
    return NewList


List = ['A', 1, 'B', 2, 'C', 3]
print(ToDictList(List))
