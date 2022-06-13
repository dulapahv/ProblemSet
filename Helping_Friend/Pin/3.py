def LeftRotate(numList, numRotate):
    temp = []
    for i in range(numRotate):
        temp += numList[i]
    for i in range(len(temp)):
        numList.remove(temp[i])
        numList.append(temp[i])
    return numList

def RightRotate(numList, numRotate):
    temp = []
    for i in range(numRotate):
        temp += numList[len(numList) - i - 1]
    return temp


usin = input("Enter 5 inputs: ").split(" ")
numRotate = eval(input("Enter an integer number of rotations (0-4): "))
if type(numRotate) == int and 0 <= numRotate <= 4:
    print(f"The left-rotated list: {LeftRotate(usin, numRotate)}")
    print(f"The right-rotated list: {RightRotate(usin, numRotate)}")
else:
    print("Error!")