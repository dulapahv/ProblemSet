class Solution:
    def mostWordsFound(self, sentences):
        ret = 0
        for sentence in sentences:
            word = sentence.count(' ') + 1
            if word > ret:
                ret = word
        return ret


print(Solution().mostWordsFound(
    ["please wait", "continue to fight", "continue to win"]))
