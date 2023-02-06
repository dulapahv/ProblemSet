class Solution(object):
    def myPow(self, x, n):
        factor = x
        if (n > 0):
            while n > 1:
                x *= factor
                n -= 1
        else:
            while n <= 0:
                x /= factor
                n += 1
        return x


print(Solution().myPow(2.1, 3))
