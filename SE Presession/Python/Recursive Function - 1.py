def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)


FirstNum = int(input("First Number: "))
SecondNum = int(input("Second Number: "))
print(GCD(FirstNum, SecondNum))
