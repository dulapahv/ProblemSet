usin = ""
while usin != "X" and not usin.isdigit():
    usin = input("Enter an integer number ('X' to exit): ")

if usin == "X":
    exit(0)
for i in range(int(usin)):
    for j in range(int(usin)):
        if i == j:
            print("X", end = " ")
        elif int(usin) - i - 1 == j:
            print("X", end = " ")
        else:
            print(".", end = " ") 
    print()