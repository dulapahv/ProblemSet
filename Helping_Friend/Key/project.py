foodDatabase = {
    "กระเพราหมูสับ": ["rice", "pork", "basil", "oily", "spicy"],
    "กระเพราไก่": ["rice", "chicken", "basil", "oily", "spicy"],
    "กระเพราปลาหมึก": ["rice", "squid", "basil", "oily", "spicy"],
    "กระเพราเนื้อ": ["rice", "meat", "basil", "oily", "spicy"],
    "ข้าวมันไก่" : ["rice", "chicken", "cucumber"],
    "ข้าวหน้าเป็ด" : ["rice", "duck", "coriander"],
    "ข้าวไข่เจียว": ["rice", "egg", "oily"],
    "ข้าวผัดหมู": ["rice", "pork", "egg", "oily"],
    "ข้าวผัดแหนม": ["rice", "pork", "egg", "oily"],
    "ข้าวผัดกุ้ง": ["rice", "shrimp", "egg", "oily"],
    "สปาเก็ตตี้มะเขือเทศ": ["pasta", "tomato" ,"onion", "pork"],
    "สปาเก็ตตี้คาโบนาร่า": ["pasta", "cheese", "ham", "egg"],
    "มาม่าผัดหมูสับใส่ใข่": ["noodle", "egg", "pork", "oily"],
    "ข้าวหน้าหมู": ["rice", "pork", "egg"],
    "ข้าวหน้าไก่": ["rice", "chicken", "egg"],
    "ข้าวหมูกระเทียม": ["rice", "pork", "garlic"],
    "ก๋วยเตี๋ยวต้มยำ": ["noodle", "soupy", "spicy", "pork"],
    "ขนมจีนน้ำยา": ["noodle", "soupy", "spicy"],
    "กุ้งอบวุ้นเส้น": ["noodle", "shrimp", "spicy"],
    "ข้าวไข่ตุ๋น": ["rice", "egg", "coriander"],
    "ผัดวุ้นเส้น": ["noodle", "shrimp", "pork", "tomato", "coriander", "egg", "spring onion", "oily"],
    "ยำวุ้นเส้นหมูยอ": ["noodle", "pork", "coriander", "spring onion", "tomato", "spicy"],
    "ยำวุ้นเส้นกุ้งสด": ["noodle", "shrimp", "coriander", "spring onion", "tomato", "spicy"],
    "ข้าวต้มหมู": ["rice", "pork", "soupy"],
    "ข้าวต้มปลา": ["rice", "fish", "soupy"],
    "ข้าวต้มหมูสับ": ["rice", "pork", "soupy"],
    "โจ้กหมูสับ": ["rice", "pork", "soupy"],
    "ลาบหมู": ["pork", "onion", "basil", "spicy"],
    "ส้มตำ": ["papaya", "spicy"],
    "คะน้าหมูกรอบ": ["pork", "collard", "spicy", "oily"],
    "ผัดซีอิ๊วกุ้ง": ["noodle", "shrimp", "collard", "spicy", "oily", "egg"],
    "ผัดซีอิ๊วหมู": ["noodle", "pork", "collard", "spicy", "oily", "egg"],
    "ผัดไทย": ["noodle", "shrimp", "oily", "egg"],
    "แซนวิช": ["ham", "bread", "cheese", "egg"],
    "ขนมปังกระเทียม": ["bread", "garlic", "cheese", "egg"],
    "ขนมปังหน้าไข่อบชีส": ["bread", "cheese", "egg"],
    "ขนมปังชุบไข่ทอด": ["bread", "egg", "oily"],

}

carbDatabase = {"rice", "noodle", "bread", "pasta"}
dairyDatabase = {"egg", "cheese"}
meatDatabase = {"ham", "pork", "beef", "chicken", "fish", "shrimp", "squid"}
vegDatabase = {"papaya", "basil", "onion", "coriander", "cucumber", "tomato", "collard", "garlic", "spring onion"}
ETCDatabase = {"soupy", "spicy", "oily"}


"""Ask user for ingredients they like"""
def ask(allList, text, amount=2):  # Modify 'amount' to change how many ingredient to ask user in each question
    chosenList = []
    allList = list(allList)
    start = 0
    end = amount
    for i in range(len(allList) // amount):
        usin = input(f"Which {text} do you prefer {allList[start:end]} or 'none'? (coma separated)\n> ").lower().replace(" ", "").split(",")
        if "none" not in usin:
            for ingredient in usin:
                chosenList.append(ingredient)
        start += amount
        end += amount

    if len(allList) % amount != 0:
        usin = input(f"Which {text} do you prefer {allList[start:]} or 'none'? (coma separated)\n> ").lower().replace(" ", "").split(",")
        if "none" not in usin:
            for ingredient in usin:
                chosenList.append(ingredient)
    return chosenList


"""Create a rank of food based on user chosen ingredient"""
def sort(database, data):
    rank = {}
    for item in database:
        rank[item] = 0
        for ingredient in data:
            if ingredient in database[item]:
                rank[item] += 1
    return rank


"""Print out the food in order of rank"""
def display(rank, amount):
    for index, food in enumerate(sorted(rank, key=rank.get, reverse=True)):
        if index + 1 <= amount:
            print(f"{index + 1}. {food}")


chosenIngredient = ask(carbDatabase, "CARBOHYDRATE")
chosenIngredient += ask(dairyDatabase, "DAIRY PRODUCTS")
chosenIngredient += ask(meatDatabase, "MEAT")
chosenIngredient += ask(vegDatabase, "VEGETABLE")
chosenIngredient += ask(ETCDatabase, "ADDITIONAL PROPERTY", len(ETCDatabase))

# print(f"{chosenIngredient=}")  # debug for viewing chosen ingredients
foodRank = sort(foodDatabase, chosenIngredient)

# print(f"{foodRank=}")  # debug for viewing score of each food
print("\n=======================================")
print("Food ranking based on your preferences:")
display(foodRank, 10)  # Modify this number to change the amount of food to be selected
