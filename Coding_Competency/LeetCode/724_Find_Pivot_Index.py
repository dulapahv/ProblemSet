class Solution(object):
    def pivotIndex(self, nums):
        default = -1
        sum1 = nums.copy()
        sum2 = nums.copy()[::-1]
        for i in range(1, len(nums)):
            sum1[i] += sum1[i - 1]
        for i in range(1, len(nums)):
            sum2[i] += sum2[i - 1]
        print(sum1)
        print(sum2)
        if sum1[0] == sum2[-1] or sum1[-1] == sum2[0]:
            return 0
        for i in range(len(sum1) - 1):
            if (sum1[i + 1] == sum2[i] or sum2[i + 1] == sum1[i]):
                if i + 2 >= len(sum1) - 1:
                    return -1
                return i + 2
        return default


print(Solution().pivotIndex([-1,-1,-1,-1,0,1]))
