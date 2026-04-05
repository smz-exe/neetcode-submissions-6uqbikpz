class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n  in hashset:
            if n - 1 not in hashset:
                c, k = 1, n
                while True:
                    k += 1
                    if k in hashset:
                        c += 1
                    else:
                        res = max(res, c)
                        break
        return res



