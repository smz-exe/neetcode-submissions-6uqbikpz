class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            
            candidates = (
                n, 
                n * cur_min,
                n * cur_max
            )

            cur_min = min(candidates)
            cur_max = max(candidates)

            res = max(res, cur_max)
        
        return res
