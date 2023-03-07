from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        arr = [nums]
        for i in range(len(nums) - 1):
            temp = []
            for j in range(len(arr[i]) - 1):
                temp.append((arr[i][j] + arr[i][j + 1]) % 10)
            arr.append(temp)
        return arr[-1][0]


print(Solution().triangularSum([5]))
