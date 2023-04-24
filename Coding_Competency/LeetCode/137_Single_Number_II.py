from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [num for num in nums if nums.count(num) == 1][0]


print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
