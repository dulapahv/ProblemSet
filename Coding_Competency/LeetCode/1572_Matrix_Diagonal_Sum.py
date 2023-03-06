from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat[0])
        if l == 1:
            return mat[0][0]
        count = 0 if l % 2 == 0 else 1
        for i in range(1, l, 2):
            count += 4
        ret = 0
        times = count - l
        if count % 2 == 0:
            for i in range(times):
                ret += mat[i][i]
            for i in range(times):
                ret += mat[l - i - 1][i]
        else:
            mid = l // 2
            for i in range(times + 1):
                ret += mat[i][i]
            for i in range(times + 1):
                if i != mid:
                    ret += mat[l - i - 1][i]
        return ret


print(Solution().diagonalSum([[7, 9, 8, 6, 3],
                              [3, 9, 4, 5, 2],
                              [8, 1, 10, 4, 10],
                              [9, 5, 10, 9, 6],
                              [7, 2, 4, 10, 8]]))
