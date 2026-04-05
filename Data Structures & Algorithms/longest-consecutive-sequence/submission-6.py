class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sortedList = sorted(nums)
        res = 1
        c = 1
        for i in range(len(sortedList)-1):
            if sortedList[i+1] - sortedList[i] > 1:
                c = 1
            if sortedList[i+1] - sortedList[i]  == 1:
                c += 1
            res = max(res, c)
        return res

