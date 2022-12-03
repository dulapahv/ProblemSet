class Solution(object):
    def runningSum(self, nums):
        ls = []
        for i in range(len(nums)):
            ls.append(sum(nums[:i + 1]))
        return ls


print(Solution().runningSum([3,1,2,10,1]))
