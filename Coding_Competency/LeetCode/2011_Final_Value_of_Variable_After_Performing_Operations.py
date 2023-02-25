class Solution:
    def finalValueAfterOperations(self, operations):
        i = 0
        for op in operations:
            if op == "X++" or op == "++X":
                i += 1
            else:
                i -= 1
        return i

print(Solution().finalValueAfterOperations(["++X","++X","X++"]))