from abc import ABC, abstractmethod

class Goods(ABC):
    @abstractmethod
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @abstractmethod
    def get_cost(self):
        pass

class StationaryGood(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def get_cost(self):
        return self.price * self.quantity


class Magazine(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def get_cost(self):
        return self.price * self.quantity


class Book(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def get_cost(self):
        return self.price * self.quantity * 0.9  # 10% discount


class Ribbon(Goods):
    def __init__(self, color, length):
        super().__init__(color, 5, length)  # 5 THB/1 meter
    
    def get_cost(self):
        return self.price * self.quantity 


def getTotalCost(basket):
    total = 0
    for goods in basket:
        total += goods.get_cost()
    return f"Total cost is ${total:.2f}"
