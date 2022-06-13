str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")

chk1, chk2 = 0, 0
if len(str1) < len(str2):
    for i in range(len(str2)):
        if chk1 == 1:
            break
        if str2[i - 1] == str1[0]:
            for j in range(len(str1)):
                if str2[i + j] != str1[j]:
                    chk1 = 1
                    print("Result : First string is a substring of the second string")
                    break
                else:
                    chk1 = 0
    if chk1 == 0:
        print("Result : First string is not a substring of the first string")
else:
    for i in range(len(str1)):
        if chk2 == 1:
            break
        if str1[i - 1] == str2[0]:
            for j in range(len(str2)):
                if str1[i + j] != str2[j]:
                    chk2 = 1
                    print("Result : Second string is a substring of the first string")
                    break
                else:
                    chk2 = 0
    if chk2 == 0:
        print("Result : Second string is not a substring of the first string")