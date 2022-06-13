money = int(input("How much you want to withdraw: "))
moneyTypes = [1000, 500, 100]
for i in range(len(moneyTypes)):
    if money // moneyTypes[i] != 0:
        if money // moneyTypes[i] != 1 and i == 0:
            print(f"You get: {money // moneyTypes[i]} notes of " +
            f"{moneyTypes[i]:,} Bahts")
        elif money // moneyTypes[i] != 1:
            print(f"{money // moneyTypes[i]:>10} notes of " +
            f"{moneyTypes[i]:,} Bahts")
        else:
            print(f"{money // moneyTypes[i]:>10} note of "
            f"{moneyTypes[i]:,} Bahts")
    money %= moneyTypes[i]