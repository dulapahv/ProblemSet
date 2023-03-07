from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    print(i, j)
                    count += 1
        return count


print(Solution().countPairs([1,2,3,4], 1))
