firstName = input("Enter you first name : ")
lastName = input("Enter your last name : ")
gender = input("Enter your gender (m/f) : ")

print(f"{gender.upper()}{lastName[0].upper()}{firstName[:6].upper()}")