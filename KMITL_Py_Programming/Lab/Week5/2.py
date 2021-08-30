usin = (eval(input("Enter Number: ")))
if(isinstance(usin, float)):
    print("How do you want to display the number?\n1. Floating point\n2. Scientific")
    choice = int(input("Choice: "))
    if choice == 1:
        print(f"Result: {usin}")
    elif choice == 2:
        print(f"Result: {usin:e}")
    else:
        print("Invalid choice")
elif(isinstance(usin, int)):
    print("How do you want to display the number?\n1. Binary\n2. Octal\n3. Hexadecimal\n4. Decimal")
    choice = int(input("Choice: "))
    if choice == 1:
        print(f"Result: {usin:b}")
    elif choice == 2:
        print("Result:", oct(usin).removeprefix("0o"))
    elif choice == 3:
        print("Result:", hex(usin).removeprefix("0x"))
    elif choice == 4:
        print(f"Result: {usin}")
    else:
        print("Invalid choice")