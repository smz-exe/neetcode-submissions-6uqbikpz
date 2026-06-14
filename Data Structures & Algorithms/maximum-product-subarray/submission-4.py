class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_min = cur_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            candidates = (
                num,
                num * cur_min,
                num * cur_max
            )

            cur_min = min(candidates)
            cur_max = max(candidates)
            res = max(res, cur_max)
        
        return res