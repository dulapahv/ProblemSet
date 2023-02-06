class Solution(object):
    def shuffle(self, nums, n):
        ret = []
        i = 0
        for index in range(len(nums)):
            if index % 2 == 0:
                ret.append(nums[i])
                i += 1
            else:
                ret.append(nums[n]);
                n += 1
        return ret


print(Solution().shuffle([1, 1, 2, 2], 2))
