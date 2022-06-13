chk = 0
for i in range(50):
    if i % 3 != 0:
        if i != 49:
            if chk % 2 != 0:
                print(50 - i - 1, end = ", ")                
            else:
                print(50 - i, end = ", ")
            chk += 1
        else:
            print(50 - i, end = ".")
