n = int(input("enter no. of lines: "))
if n < 0:
    print("Error")
else:
    for x in range(1, n+1, 1):
        if x % 2 == 1:
            print("-" * x)
        else:
            print("*" * x)