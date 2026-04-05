class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l, r = r, r + 1
            else:
                res = max(res, profit)
                r += 1
        return res

                

