print("Please enter a time in 24 hour format.")

hour = int(input("Hours: "))
minute = int(input("Minutes: "))
second = int(input("Seconds: "))

sign = "AM"

if hour >= 12:
    sign = "PM"
    hour -= 12
print(f"The time you just entered in 12 hour format is {hour:02d}:{minute:02d}:{second:02d} {sign}.")