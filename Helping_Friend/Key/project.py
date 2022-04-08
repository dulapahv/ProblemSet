import random

foodDatabase = {
    "กระเพราไข่ดาว": ["rice", "pork", "egg", "basil", "onion"],
    "ข้าวไข่เจียว": ["rice", "egg"],
    "คาโบนารา": ["noodle", "pork", "egg"],
    "ปลากระพงทอดน้ำปลา": ["rice", "fish", "celery", "onion"],
    "ข้าวหน้าหมูคัตสึดง": ["rice", "pork", "onion", "egg"],
    "ทาโกะยากิ": ["squid", "carrot"],
    "ราเมน": ["noodle", "celery", "onion", "egg", "pork"],
    "ซูชิ": ["rice", "cucumber", "fish"],
    "ไข่ตุ๋น": ["egg", "shrimp", "pork", "celery"],
    "ผัดวุ้นเส้น": ["noodle", "shrimp", "pork", "onion"],
    "ผัดฟักทอง": ["pumpkin", "onion", "celery", "egg"],
    "ข้าวต้มปลา": ["fish", "rice", "onion", "onion"],
    "ลาบหมู": ["pork", "onion", "basil", "celery"],
}

vegetableList = ["basil", "celery", "onion", "carrot", "cucumber"]

"""Create a list of unique ingredients from the food database"""
ingredientList = ["vegetable"]
for ingredient in foodDatabase.values():
    ingredientList.extend(ingredient)
randomIngredientList = list(set(ingredientList))

"""Select a specified amount of random ingredient from the unique ingredients list to ask user"""
amount = 3  # Change this number to modify the amount of random ingredient to be selected

randomChosenIngredientList = []
n = 0
while n != amount:
    if randomIngredientList[n] not in vegetableList and randomIngredientList[n] not in randomChosenIngredientList:
        randomChosenIngredientList.append(randomIngredientList[n])
        n += 1
    else:
        randomIngredientList = random.sample(ingredientList, amount)

"""Prompt user to deicide the ingredients they prefer"""
chosenIngredientList = randomChosenIngredientList.copy()
for ingredient in randomChosenIngredientList:
    usin = input(f"Do you like {ingredient}? (y/n) ").lower()
    if usin == "n":
        chosenIngredientList.remove(ingredient)
    elif ingredient == "vegetable" and usin == "y":
        print(*vegetableList, sep=", ")
        usinVegtetable = input(f"What vegetables do you like? (separated by coma) ").lower().replace(" ", "").split(",")
        for veg in usinVegtetable:
            chosenIngredientList.append(veg)
        chosenIngredientList.remove(ingredient)

"""Create a rank of food based on user chosen ingredient"""
rank = {}
for food in foodDatabase:
    rank[food] = 0
    for ingredient in chosenIngredientList:
        if ingredient in foodDatabase[food]:
            rank[food] += 1

# print(rank)  # debug for viewing score of each food

for index, food in enumerate(sorted(rank, key=rank.get, reverse=True)):
    print(f"{index + 1}. {food}")