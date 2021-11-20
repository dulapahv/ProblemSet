def UserInput():
    numList = []
    usin = ""
    while usin != "Done":
        usin = input("Enter an input: ")
        if usin != "Done":
            numList.append(int(usin))
        else:
            return numList

def SumOut(numList):
    print(f"The summation is {sum(numList)}")

def MinOut(numList):
    print(f"The minimum is {min(numList)}")

def MaxOut(numList):
    print(f"The maximum is {max(numList)}")

numList = UserInput()
SumOut(numList)
MinOut(numList)
MaxOut(numList)