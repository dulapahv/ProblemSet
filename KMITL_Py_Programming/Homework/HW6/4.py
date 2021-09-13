number = int(input("Enter a number: "))
numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numArr1 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] # -1
numArr2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] # -1

if 0 <= number <= 9 or 101 <= number <= 109:
    if 101 <= number <= 109:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr[int(str(number)[2])]}")
    else:
        print(numArr[number])
elif 11 <= number <= 19 or 111 <= number <= 119:
    if 111 <= number <= 119:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr1[int(str(number)[2]) - 1]}")
    else:
        print(f"{numArr1[int(str(number)[1]) - 1]}")
elif number % 10 == 0:
    if number < 100:
        print(f"{numArr2[int(str(number)[0]) - 1]}")
    elif number >= 110:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}")
    else:
        print(f"{numArr[int(str(number)[0])]} hundred")
elif 21 <= number <= 99 or 121 <= number <= 999:
    if 101 <= number <= 999:
        print(f"{numArr[int(str(number)[0])]} hundred and {numArr2[int(str(number)[1]) - 1]}-{numArr[int(str(number)[2])]}")
    else:
        print(f"{numArr2[int(str(number)[0]) - 1]}-{numArr[int(str(number)[1])]}")   
else:
    print("I don't know.")