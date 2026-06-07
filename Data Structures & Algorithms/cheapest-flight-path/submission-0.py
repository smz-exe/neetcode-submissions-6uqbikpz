import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        max_flights = k + 1
        graph = {i: [] for i in range(n)}

        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        
        dist = {i: [float("inf")] * (max_flights + 1) for i in range(n)}
        dist[src][0] = 0

        min_heap = [(0, src, 0)] # cost, city, flights_used

        while min_heap:
            cost, city, flights_used = heapq.heappop(min_heap)

            if city == dst:
                return cost
            
            if flights_used == max_flights:
                continue
            
            if dist[city][flights_used] < cost:
                continue
            
            for next_city, price in graph[city]:
                next_cost = cost + price
                next_flights_used = flights_used + 1

                if next_cost < dist[next_city][next_flights_used]:
                    dist[next_city][next_flights_used] = next_cost
                    heapq.heappush(
                        min_heap,
                        (next_cost, next_city, next_flights_used)
                    )
        
        return -1
