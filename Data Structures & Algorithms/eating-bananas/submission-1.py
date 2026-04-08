class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxNum = 0
        for p in piles:
            maxNum = max(maxNum, p)
        
        l = 1
        r = maxNum
        res = maxNum
        while l <= r:
            mid = l + (r - l) // 2
            
            hours = 0
            for p in piles:
                hours += p // mid if p % mid == 0 else p // mid + 1
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res