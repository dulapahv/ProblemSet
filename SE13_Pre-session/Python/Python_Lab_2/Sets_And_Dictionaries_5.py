original = ["A", 1, "B", 2, "C", 3]
key = ["Name", "Number"]
n = len(original)
ans = []
for i in range(0, n, 2):
    ans.append({key[0]: original[i], key[1]: original[i + 1]})
print("The constructed dictionary list : " + str(ans))

# Another solution
# def ToDictList(InputList):
#     Dict = {'Name': None, 'Number': None}
#     NewList = []
#     for i in range(int(len(InputList) / 2)):
#         Dict.update({'Name': InputList[i * 2]})
#         Dict.update({'Number': InputList[(i * 2) + 1]})
#         NewList.append(Dict.copy())
#     return NewList
#
#
# List = ['A', 1, 'B', 2, 'C', 3]
# print(ToDictList(List))
