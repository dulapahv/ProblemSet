speed = input("Enter speed in mph: ")
if speed.isdigit() == False:
    print("Invalid input")
    exit(0)
distance = input("Enter distance in miles: ")
if distance.isdigit() == False:
    print("Invalid input")
    exit(0)
output = input("Enter output format (D or M): ")
if output != "D" and output != "M":
    print("Invalid input")
    exit(0)
else:
    hourDec = int(distance) / int(speed)
    hour = int(distance) // int(speed)
    minute = int((hourDec * 60) % 60)

    print(f"At {speed} mph, it will take")
    if output == "D":
        print(f"{hourDec} hours to travel {distance} miles.")
    else:
        print(f"{hour} hours and {minute} minutes to travel {distance} miles.")