class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_min = cur_max = nums[0]

        for n in nums[1:]:
            if n == 0:
                cur_min, cur_max = 1, 1
            
            candidates = (
                n,
                n * cur_min,
                n * cur_max
            )

            cur_min = min(candidates)
            cur_max = max(candidates)
            res = max(res, cur_max)

        return res