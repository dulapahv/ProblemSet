from abc import ABC, abstractmethod

class Transportation(ABC):
    @abstractmethod
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def find_cost():
        pass


class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    
    def find_cost(self):
        return 0 # cost is 0


class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        return 40 * self.distance # 40 THB/km


class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station
    
    def find_cost(self):
        return 5 * self.station # 5 THB/station

walk = Walk("KMITL", "KMITL SCB Bank", 0.6)
print(f"Walk = {walk.find_cost()} THB")
taxi = Taxi("KMITL SCB Bank", "Ladkrabang Station", 5)
print(f"Taxi = {taxi.find_cost()} THB")
train = Train("Ladkrabang Station", "Payathai Station", 40, 6)
print(f"Train = {train.find_cost()} THB")
taxi = Taxi("Payathai Station", "The British Council", 3)
print(f"Taxi = {taxi.find_cost()} THB")