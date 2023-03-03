class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ret = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            ret.append(count)
        return ret


print(Solution().smallerNumbersThanCurrent([7, 7, 7, 7]))
