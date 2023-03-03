class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        separated = [int(elem) for elem in str(n)]
        prod = 1
        add = 0
        for num in separated:
            prod *= num
            add += num
        return prod - add


print(Solution().subtractProductAndSum(4421))
