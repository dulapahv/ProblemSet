number = int(input("Enter a number: "))
numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numArr1 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numArr2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if number <= 9:
    print(f"{numArr[number]}")
elif 11 <= number <= 19:
    print(f"{numArr1[int(str(number)[1]) - 1]}")
elif int(str(number)[1]) == 0 and number <= 99:
    print(f"{numArr2[int(str(number)[0]) - 1]}")
elif 21 <= number <= 99:
    print(f"{numArr2[int(str(number)[0]) - 1]}-{numArr[int(str(number)[1])]}") 
elif int(str(number)[1]) == 0:
    if int(str(number)[2]) == 0:
        print(f"{numArr[int(str(number)[0])]} hundred")
    else:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr[int(str(number)[2])]}")
elif 111 <= number <= 119:
    print(f"{numArr[int(str(number)[0])]} hundred and {numArr1[int(str(number)[2]) - 1]}")
elif int(str(number)[2]) == 0 and number <= 999:
    print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}")
elif 121 <= number <= 999:
    if int(str(number)[1]) == 1:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr1[int(str(number)[2]) - 1]}")
    else:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}-{numArr[int(str(number)[2])]}")
else:
    print("I don't know.")