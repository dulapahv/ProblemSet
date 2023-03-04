class Solution:
    def createTargetArray(self, nums, index):
        ret = []
        for i in range(len(nums)):
            ret.insert(index[i], nums[i])
        return ret


print(Solution().createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
