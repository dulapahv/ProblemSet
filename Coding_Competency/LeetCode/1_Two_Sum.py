class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return list([i, j])

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))