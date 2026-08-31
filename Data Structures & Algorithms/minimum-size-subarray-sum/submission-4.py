class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        l, r = 0, 0
        res = float("inf")
        for i, num in enumerate(nums):
            cur += num
            r += 1
            print(l, r, cur)

            if cur >= target:
                res = min(res, r - l)

            while cur - nums[l] >= target:
                cur -= nums[l]
                l += 1
                res = min(res, r - l)
            
            print(l, r, cur, res)
        
        return res if res != float("inf") else 0
            