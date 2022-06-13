num = []
for char in input():
    if char.isdigit(): num.append(int(char))
print(list(set(num)))

# Input = [(1, 3, 4, 5), (4, 5, 7), (1, 2, 4)]
# sec = []
# for array in Input:
#     for nums in array:
#         if nums not in sec:
#             sec.append(nums)
#             sec.sort()
# print(sec)

# UserInput = input("Input: ")
# SetInput = set(UserInput)
# ListInput = list(SetInput)
# result = []
# for i in range(len(ListInput)):
#     if ListInput[i] == "[" or ListInput[i] == "]" or ListInput[i] == "(" or ListInput[i] == ")" or ListInput[i] == "," or ListInput[i] == " ":
#         pass
#     else:
#         result.append(int(ListInput[i]))
#
# print(sorted(result))

12