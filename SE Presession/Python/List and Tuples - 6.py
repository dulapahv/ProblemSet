UserInput = input("Input: ")
SetInput = set(UserInput)
ListInput = list(SetInput)
result = []
for i in range(len(ListInput)):
    if ListInput[i] == "[" or ListInput[i] == "]" or ListInput[i] == "(" or ListInput[i] == ")" or ListInput[i] == "," or ListInput[i] == " ":
        pass
    else:
        result.append(int(ListInput[i]))

print(sorted(result))