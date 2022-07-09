money = int(input("Input your amount of money: "))
moneyTypes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

for i in range(len(moneyTypes)):
	if money // moneyTypes[i] != 0:
		if moneyTypes[i] > 10:
			print(f"{moneyTypes[i]}-Baht notes: {money // moneyTypes[i]}")
		else:
			print(f"{moneyTypes[i]}-Baht coins: {money // moneyTypes[i]}")
	money = money % moneyTypes[i]
