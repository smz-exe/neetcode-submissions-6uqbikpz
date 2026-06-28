class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo: dict[tuple[int, bool], int] = {}

        def dfs(i: int, can_buy: bool) -> int:
            if i >= len(prices):
                return 0
            
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            
            if can_buy:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                memo[(i, can_buy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, False)
                memo[(i, can_buy)] = max(sell, cooldown)
            
            return memo[(i, can_buy)]
        
        return dfs(0, True)