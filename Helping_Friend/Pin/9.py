inputList = []
for i in range(9):
    usin = input("Input: ")
    if usin != "x" and usin != "o":
        print("Wrong input")
        exit(1)
    inputList.append(usin)

print("-------")
for i in range(3):
    for j in range(3):
        print(f"|{inputList[i+j]}", end = "")
    print("|")
    print("-------")