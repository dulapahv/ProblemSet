from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        plant = 0
        store = capacity
        while plant < len(plants):
            if capacity - plants[plant] >= 0:
                steps += 1
                capacity -= plants[plant]
                plant += 1
            else:
                steps += plant * 2
                capacity = store
        return steps


print(Solution().wateringPlants([1, 1, 1, 4, 2, 3], 4))
