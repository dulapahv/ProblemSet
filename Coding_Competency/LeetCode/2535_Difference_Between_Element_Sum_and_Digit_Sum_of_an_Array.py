class Solution:
    def differenceOfSum(self, nums):
        return sum(nums) - sum([int(char) for char in str(nums) if ord(char) >= ord('0') and ord(char) <= ord('9')])


print(Solution().differenceOfSum([1, 2, 3, 4]))
