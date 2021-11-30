import csv

fileName = input("Enter file name: ")
with open(fileName, "r") as file:
    cart = csv.reader(file)
    price = 0
    quantity = 0
    for row in cart:
        try:
            price += float(row[0]) * float(row[1])
            quantity += float(row[1])
        except:
            pass
print(f"There are {quantity:.0f} items in the cart")
print(f"Total amount is {price:.2f} baht")