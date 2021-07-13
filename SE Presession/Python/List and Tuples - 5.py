Tuple = (7, 8, 9)
List = [1, 2, 3]
newList = list(Tuple)
CombinedList = newList + List
Result = tuple(CombinedList)
print(Result)