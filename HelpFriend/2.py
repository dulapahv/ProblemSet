class House:
    def __init__(self, color = "", nationality = "", pet = "", drinks = "", cig_brand = ""):
        self.__color = color
        self.__nationality = nationality
        self.__pet = pet
        self.__drinks = drinks
        self.__cig_brand = cig_brand

    def addColor(self, new_color):
        self.__color = new_color

    def addNationality(self, new_nationality):
        self.__nationality = new_nationality

    def addPet(self, new_pet):
        self.__pet = new_pet

    def addDrinks(self, new_drinks):
        self.__drinks = new_drinks

    def addCigBrand(self, new_cig_brand):
        self.__cig_brand = new_cig_brand

    def allAttribute(self):
        return self.__color, self.__nationality, self.__pet, self.__drinks, self.__cig_brand

    def getColor(self):
        return self.__color

    def getNationality(self):
        return self.__nationality

    def getPet(self):
        return self.__pet

    def getDrinks(self):
        return self.__drinks

    def getCigBrand(self):
        return self.__cig_brand

# main
house1 = House()
house2 = House()
house3 = House()
house4 = House()
house5 = House()

# know for sure
# analyse 1
house1.addNationality("Norwegian")
house2.addColor("Blue")
house3.addDrinks("Milk")
house4.addColor("Green")
house5.addColor("White")
house1.addColor("Yellow")
house3.addNationality("Brit")
house3.addColor("Red")
house4.addDrinks("Coffee")
house1.addCigBrand("Dunhill")
house2.addPet("Horses")

house1.addPet("Cats")
house2.addCigBrand("Blends")
house3.addCigBrand("Pall Mall")
house4.addNationality("German")
house5.addCigBrand("Blue Master")

arr = [house1, house2, house3, house4, house5]
for i in range(len(arr)):
    if arr[i].getNationality() == "" and arr[i].getPet() == "":
        if arr[i - 1].getNationality() == "Swede" and arr[i - 1].getPet() == "Dogs":
            continue
        else:
            arr[i].addNationality("Swede")
            arr[i].addPet("Dogs")
    if arr[i].getNationality() == "" and arr[i].getDrinks() == "":
        arr[i].addNationality("Dane")
        arr[i].addDrinks("Tea")
    if arr[i - 1].getCigBrand() == "Pall Mall" and arr[i - 1].getPet() == "":
        arr[i - 1].addPet("Birds")
    if arr[i - 1].getCigBrand() == "Blue Master" and arr[i - 1].getDrinks() == "":
        arr[i - 1].addDrinks("Beer")
    if arr[i - 1].getNationality() == "German" and arr[i - 1].getCigBrand() == "":
        arr[i - 1].addCigBrand("Prince")
    if arr[i - 1].getPet() == "Cats" and arr[i].getCigBrand() == "":
        arr[i].addCigBrand("Blends")
    if arr[i - 1].getCigBrand() == "Blends" and arr[i].getPet() == "":
        arr[i - 1].addPet("Cats")
    if arr[i].getCigBrand() == "Blends" and arr[i - 1].getDrinks() == "" and arr[i + 1].getDrinks() != "":
        arr[i - 1].addDrinks("Water")
    if arr[i].getCigBrand() == "Blends" and arr[i + 1].getDrinks() == "" and arr[i - 1].getDrinks() != "":
        arr[i + 1].addDrinks("Water")

print("Answer: ", end='')
for i in range(len(arr)):
    if arr[i].getPet() == "":
        arr[i].addPet("Fish")
        print(f"House {i + 1} owns the {arr[i].getPet()}.")