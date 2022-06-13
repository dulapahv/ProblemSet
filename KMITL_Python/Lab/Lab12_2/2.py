def find_duplicates(dict):
    duplicateList = {}
    keyList = []
    for key, value in dict.items():
        keyList.append(value)
    keyList = set([name for name in keyList if keyList.count(name) > 1])
    for key, value in dict.items():
        if value in keyList:
            duplicateList.update({key: value})
    return duplicateList


myDict = {"s5301":"Fred", "s5302":"Harry", "s5303":"John", "s5304":"Fred", "s5305":"Harry"}
print(find_duplicates(myDict))
