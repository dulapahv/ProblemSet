number = int(input("Enter a number: "))
numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numArr1 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] # -1
numArr2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] # -1

if 0 <= number <= 9:
    print(f"{numArr[number]}")
elif 10 <= number <= 19:
    if number == 10:
        print(f"{numArr2[0]}")
    else:
        print(f"{numArr1[int(str(number)[1]) - 1]}")
elif 20 <= number <= 99:
    if number % 10 == 0:
        print(f"{numArr2[int(str(number)[0]) - 1]}")
    else:
        print(f"{numArr2[int(str(number)[0]) - 1]}-{numArr[int(str(number)[1])]}") 
elif 100 <= number <= 109:
    if number == 100:
        print(f"{numArr[1]} hundred")
    else:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr[int(str(number)[2])]}")
elif int(str(number)[1]) == 1:
    if number == 110:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[0]}")
    else:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr1[int(str(number)[2]) - 1]}")
elif 120 <= number <= 999:
        if number % 10 == 0:
            print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}")
        elif int(str(number)[1]) == 0:
            print(f"{numArr[int(str(number)[0])]} hundred and {numArr[int(str(number)[2])]}")
        else:
            print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}-{numArr[int(str(number)[2])]}")
else:
    print("I don't know.")