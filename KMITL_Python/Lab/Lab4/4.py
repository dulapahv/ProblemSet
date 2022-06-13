summation = 0
for i in range(5):
    integer = int(input("Enter an integer: "))
    summation += integer
    if (integer ^ summation) < 0:
        summation = integer
    print(f"Current sum: {summation}\n")