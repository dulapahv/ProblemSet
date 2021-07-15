def Factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * Factorial(n - 1)


Number = int(input("Enter the number: "))
print(Factorial(Number))
