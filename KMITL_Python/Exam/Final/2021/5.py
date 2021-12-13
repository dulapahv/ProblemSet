from abc import ABC, abstractmethod

class Sale_item(ABC):   
    @abstractmethod
    def get_cost(self):
        return self.cost

class Food(ABC):  
    @abstractmethod
    def get_cost(self):
        return self.cost

class Book(Sale_item):
    def __init__(self, name, cost, quantity = 1):
        self.name = name
        self.cost = ((cost * 75) / 100) * quantity
        self.quantity = quantity
    
    def get_cost(self):
        pass

class Appliance(Sale_item):
    def __init__(self, name, cost, quantity = 1):
        self.name= name
        self.cost = ((cost * 107) / 100) * quantity
        self.quantity = quantity

    def get_cost(self):
        pass

class Itemized_food(Food):
    def __init__(self, name, cost, quantity = 1):
        self.name = name
        self.cost = cost * quantity
        self.quantity = quantity

    def get_cost(self):
        pass

class Measured_food(Food):
    def __init__(self, name, cost, weight = 1):
        self.name = name
        self.cost = cost * weight
        self.quantity = weight

    def get_cost(self):
        pass

purchased_item = [Itemized_food("vegetable oil", 40, 2), Measured_food("mango", 70, 1.8), Book("Python", 200, 1), Appliance("rice cooker", 1200, 1)]

def calculate():
    food = 0; book = 0; appliance = 0
    for item in purchased_item:
        if (type(item) == Itemized_food or type(item) == 
            Measured_food):
            food += Food.get_cost(item)
        elif type(item) == Book:
            book += Sale_item.get_cost(item)
        elif type(item) == Appliance:
            appliance += Sale_item.get_cost(item)
    
    print(f"Total cost: {(food + book + appliance):.2f} Bahts")

calculate()