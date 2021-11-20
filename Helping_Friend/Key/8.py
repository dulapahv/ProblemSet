wellHeight = int(input("Enter the depth of the well: "))
leapHeight = int(input("How high the frog can jump up? "))
slipHeight = int(input("How far the frog slips down? "))

if leapHeight < wellHeight and leapHeight != slipHeight or wellHeight == leapHeight == slipHeight:
    day = 0
    while wellHeight > 0:
        day += 1
        wellHeight -= leapHeight
        if wellHeight > 0:
            print(f"On day {day} the frog leaps to the depth of {wellHeight} meters.")
            wellHeight += slipHeight
            print(f"At night he slips down to the depth of {wellHeight} meters.")
    print(f"The frog gets out of the well on day {day}.")
else:
    print("The frog will never escape from the well.")