class Solution(object):
    def pivotIndex(self, nums):
        ans = -1
        sum1 = nums.copy()
        sum2 = nums.copy()[::-1]
        for i in range(1, len(nums)):
            sum1[i] += sum1[i - 1]
        for i in range(1, len(nums)):
            sum2[i] += sum2[i - 1]
        print(sum1)
        print(sum2[::-1])
        for i in range(len(sum1)):
            for j in range(len(sum2)):
                if (sum1[i] == sum2[j]):
                    return i + j
        return ans

print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))