hour, minute = input("Enter time in 24 hour format: ").split(":")
if int(hour) > 12:
    hour = int(hour) - 12;
print(f"{hour}:{minute}", end=" ")
if int(hour) >= 12:
    print("PM")
else:
    print("AM")