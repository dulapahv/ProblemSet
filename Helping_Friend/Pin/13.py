shoppingCartDict = {"A": 0, "B": 0, "C": 0}
while True:
    name, amount = input("Enter two inputs: ").split()
    if name == "Exit" and int(amount) == 0:
        break
    if (name == "A" or name == "B" or name == "C") and int(amount) >= 0:
        shoppingCartDict[name] += int(amount)
    else:
        print("Wrong Input! Enter Again!")
        
for name, amount in sorted(shoppingCartDict.items()):
    print(f"The number of orders of product {name} is {amount}")