foodList = {
    "Salad": 50,
    "Soup": 80,
    "Steak": 350,
    "Wine": 830,
    "Orange Juice": 45,
    "Pasta": 160,
    "Fried rice": 165
}
cost = 0
for i in range(6):
    order = input(f"Person #{i+1} order: ")
    cost += foodList[order]
cost *= 0.13  # 13% discount
print(f"The discounted cost is {cost:.2f}")
