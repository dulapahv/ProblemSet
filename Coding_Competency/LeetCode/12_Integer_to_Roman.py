class Solution(object):
    def intToRoman(self, num):
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                 100: 'C', 500: 'D', 1000: 'M'}
        result = ""
        i = 10 * len(num)
        while num > 0:
            # 352 -> 300 + 50 + 2
            temp = num % i
            if (temp > 3):
                result += roman


print(Solution.intToRoman(3))
