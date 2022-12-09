class Solution(object):
    def threeSum(self, nums):
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        pick = sorted(list([nums[i], nums[j], nums[k]]))
                        if pick not in ans:
                            ans.append(pick)
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
