from math import floor

money = int(input("Enter money: "))
moneyTypes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

for i in range(9):
    print(moneyTypes[i], ": ", money // moneyTypes[i])
    money = money % moneyTypes[i]

# Another inefficient solution
# Check for invalid input
# def CheckInput(MoneyToCheck):
#     if MoneyToCheck == '' or MoneyToCheck < 0:
#         print("Please enter valid amount of money!")
#
#
# MoneyInput = int(input("Input your amount of money: "))
# CheckInput(MoneyInput)
#
# if MoneyInput >= 1000:
#     result = floor(MoneyInput / 1000)
#     MoneyInput -= result * 1000
#     print("1000-Baht notes:", result)
#
# if MoneyInput >= 500:
#     result = floor(MoneyInput / 500)
#     MoneyInput -= result * 500
#     print("500-Baht notes:", result)
#
# if MoneyInput >= 100:
#     result = floor(MoneyInput / 100)
#     MoneyInput -= result * 100
#     print("100-Baht notes:", result)
#
# if MoneyInput >= 50:
#     result = floor(MoneyInput / 50)
#     MoneyInput -= result * 50
#     print("50-Baht notes:", result)
#
# if MoneyInput >= 20:
#     result = floor(MoneyInput / 20)
#     MoneyInput -= result * 20
#     print("20-Baht notes:", result)
#
# if MoneyInput >= 10:
#     result = floor(MoneyInput / 10)
#     MoneyInput -= result * 10
#     print("10-Baht coins:", result)
#
# if MoneyInput >= 5:
#     result = floor(MoneyInput / 5)
#     MoneyInput -= result * 5
#     print("5-Baht coins:", result)
#
#     MoneyInput -= result * 2
#     print("2-Baht coins:", result)
#
# if MoneyInput >= 1:
#     result = floor(MoneyInput / 1)
#     MoneyInput -= result * 1
#     print("1-Baht coins:", result)
