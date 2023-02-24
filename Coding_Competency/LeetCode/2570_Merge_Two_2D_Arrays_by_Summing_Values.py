class Solution:
    def mergeArrays(self, nums1, nums2):
        num_dict = {}
        for i in nums1:
            num_dict[i[0]] = i[1]
        for i in nums2:
            if i[0] in num_dict:
                num_dict[i[0]] += i[1]
            else:
                num_dict[i[0]] = i[1]
        num_dict = list(sorted(num_dict.items(), key=lambda item: item[0]))
        ret = []
        for i in range(len(num_dict)):
            ret.append(list((num_dict[i][0], num_dict[i][1])))
        return ret


print(Solution().mergeArrays(
    [[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
