class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphamap = dict(zip([str(i) for i in range(1, 10)], [chr(c)
                        for c in range(ord('a'), ord('i') + 1)]))
        alphamap2 = dict(zip([f"{i}#" for i in range(10, 27)], [
                         chr(c) for c in range(ord('j'), ord('z') + 1)]))
        for symbol in alphamap2:
            if symbol in s:
                s = s.replace(symbol, alphamap2.get(symbol))
        for symbol in alphamap:
            if str(symbol) in s:
                s = s.replace(str(symbol), alphamap.get(symbol))
        return s


print(Solution().freqAlphabets("1326#"))
