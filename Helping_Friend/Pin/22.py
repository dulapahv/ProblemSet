dimension = int(input("Enter an integer number: "))

for i in range(dimension):
    for j in range(dimension):
        if i == 0 or i == dimension - 1:
            print("x", end = " ")
        else:
            if j == 0 or j == dimension - 1:
                print("x", end = " ")
            else:
                print(" ", end = " ")
    print()