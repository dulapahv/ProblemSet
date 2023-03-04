class Solution:
    def restoreString(self, s, indices):
        ret = ""
        for i in range(len(s)):
            ret += s[indices.index(i)]
        return ret


print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
