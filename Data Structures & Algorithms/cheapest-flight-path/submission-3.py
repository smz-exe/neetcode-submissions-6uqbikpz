class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        max_flights = k + 1

        prices = [INF] * n
        prices[src] = 0

        for _ in range(max_flights):
            next_prices = prices.copy()

            for from_city, to_city, price in flights:
                if prices[from_city] == INF:
                    continue
                
                next_prices[to_city] = min(
                    next_prices[to_city],
                    prices[from_city] + price
                )
            
            prices = next_prices
        
        return -1 if prices[dst] == INF else prices[dst]