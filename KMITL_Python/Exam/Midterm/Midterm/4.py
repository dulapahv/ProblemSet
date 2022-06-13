usin = ""
while usin != ".":
    usin = input("Please enter a character: ")
    chk = ord(usin)
    if 48 <= chk <= 57:
        print("It's a numeric character.")
    elif 65 <= chk <= 90:
        print("It's a capital letter.")
    elif 97 <= chk <= 122:
        print("It's a small-case letter.")
    else:
        print("It's a special character.")
print("Good bye.")