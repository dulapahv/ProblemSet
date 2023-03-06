from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = nums.copy()
        for num in nums:
            rev = 0
            while num > 0:
                reminder = num % 10
                rev = (rev * 10) + reminder
                num = num // 10
            new.append(rev)
        return len(set(new))


print(Solution().countDistinctIntegers([2, 2, 2]))
