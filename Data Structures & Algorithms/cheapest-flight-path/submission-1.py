class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()

            for from_city, to_city, price in flights:
                if prices[from_city] == float("inf"):
                    continue
                
                if prices[from_city] + price < temp_prices[to_city]:
                    temp_prices[to_city] = prices[from_city] + price
            prices = temp_prices

        return prices[dst] if prices[dst] != float("inf") else -1