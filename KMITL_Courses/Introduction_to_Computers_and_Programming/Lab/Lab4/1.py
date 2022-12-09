score = float(input("Enter a score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Your grade: F")
elif 50 <= score < 60:
    print("Your grade: D")
elif 60 <= score < 70:
    print("Your grade: C")
elif 70 <= score < 80:
    print("Your grade: B")
elif 80 <= score <= 100:
    print("Your grade: A")