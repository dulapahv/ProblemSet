class Solution:
    def separateDigits(self, nums):
        ret = []
        for i in nums:
            ret += [int(x) for x in list(str(i))]
        return ret


print(Solution().separateDigits([13, 25, 83, 77]))
