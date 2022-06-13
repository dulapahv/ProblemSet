name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight / (183 / 100)**2
print(f"Your body mass index (BMI) is {bmi}")

if age < 17:
    if bmi < 15:
        print(f"{name}, you are underweight.")
    elif 15 <= bmi <= 20:
        print(f"{name}, you are normal.")
    elif bmi > 20:
        print(f"{name}, you are overweight.")
elif 17 <= age <= 35:
    if bmi < 18:
        print(f"{name}, you are underweight.")
    elif 18 <= bmi <= 24:
        print(f"{name}, you are normal.")
    elif bmi > 24:
        print(f"{name}, you are overweight.")
elif age > 35:
    if bmi < 19:
        print(f"{name}, you are underweight.")
    elif 19 <= bmi <= 26:
        print(f"{name}, you are normal.")
    elif bmi > 26:
        print(f"{name}, you are overweight.")