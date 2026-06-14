class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_min = cur_max = nums[0]

        for num in nums[1:]:            
            candidates = (
                num,
                num * cur_min,
                num * cur_max
            )

            cur_min = min(candidates)
            cur_max = max(candidates)
            res = max(res, cur_max)

        return res