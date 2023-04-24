from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lst = [nums for nums in range(start, start + 2 * n, 2)]
        return reduce(lambda x, y: x ^ y, lst)


print(Solution.xorOperation(None, 5, 0))
