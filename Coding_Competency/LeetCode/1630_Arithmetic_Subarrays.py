from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        comb = []
        for i in range(len(l)):
            comb.append(sorted(nums[l[i]:r[i] + 1]))
        ret = [True] * len(comb)
        for i in range(len(comb)):
            diff = comb[i][1] - comb[i][0]
            for j in range(2, len(comb[i])):
                if comb[i][j] - comb[i][j - 1] != diff:
                    ret.pop(i)
                    ret.insert(i, False)
                    break
        return ret


print(Solution().checkArithmeticSubarrays(
    [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))
