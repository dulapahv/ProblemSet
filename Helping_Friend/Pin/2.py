def UserInput():
    numList = []
    usin = ""
    while usin != "Done":
        usin = input("Enter an input: ")
        if usin != "Done":
            if float(usin) % 1 == 0 and float(usin) >= 0:
                numList.append(int(usin))
            else:
                print("Error")
                return None
        else:
            return numList

def SumOut(numList):
    print(f"The summation is {sum(numList)}")

def MinOut(numList):
    print(f"The minimum is {min(numList)}")

def MaxOut(numList):
    print(f"The maximum is {max(numList)}")

numList = UserInput()
if numList != None:
    SumOut(numList)
    MinOut(numList)
    MaxOut(numList)