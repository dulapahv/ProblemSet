class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ret = 0
        for char in jewels:
            ret += stones.count(char)
        return ret


print(Solution().numJewelsInStones("aA", "aAAbbbb"))
