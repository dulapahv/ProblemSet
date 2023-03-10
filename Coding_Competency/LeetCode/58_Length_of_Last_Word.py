class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        for i in range(len(s) - 1, 0, -1):
            if s[i] != "":
                return len(s[i])
        return len(s[0])

print(Solution().lengthOfLastWord("sdfa"))