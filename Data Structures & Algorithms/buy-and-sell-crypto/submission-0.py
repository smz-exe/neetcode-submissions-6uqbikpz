class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l, r = 0, 1
        res = 0
 
        while l < r and r < len(prices):
            if prices[l] < prices[r]: 
                res = max(res, prices[r] - prices[l])
                r += 1
            else:
                l, r = r, r + 1
        
        return res
                

