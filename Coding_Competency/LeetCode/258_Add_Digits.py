class Solution:
    def addDigits(self, num):
        return sum(int(x) for x in list(str((sum([int(x) for x in list(str(sum([int(x) for x in list(str(num))])))])))))


print(Solution().addDigits(2147483647))
