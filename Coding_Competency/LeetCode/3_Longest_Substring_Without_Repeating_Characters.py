class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if (s == ''):
            return 0
        max = 1
        comb = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                comb.append(s[i:j])
        comb = sorted(comb)
        for i in range(1, len(comb)):
            if (len(comb[i - 1]) != len(comb[i]) or len(comb[i]) < 2):
                continue
            if (comb[i - 1] == comb[i] and comb[i - 1][0] != comb[i][1]):
                if (len(comb[i]) > max):
                    max = len(comb[i])
        print(comb)
        return max


print(Solution().lengthOfLongestSubstring("pwwkew"))
