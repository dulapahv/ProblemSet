from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        arr = [elem for elem in bank if elem.find("1") != -1]
        for i in range(1, len(arr)):
            count += arr[i].count("1") * arr[i - 1].count("1")
        return count


print(Solution().numberOfBeams(["000", "111", "000"]))
