from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, travel_time in times:
            adj[u].append((v, travel_time))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            max_time = max(time, max_time)

            for nei, travel_time in adj[node]:
                if not nei in visited:
                    heapq.heappush(min_heap, (time + travel_time, nei))
        
        return max_time if len(visited) == n else -1