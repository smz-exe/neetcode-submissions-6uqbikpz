from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        min_heap = [(0, k)]
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(min_heap, (t + w2, n2))
        
        return t if len(visited) == n else -1






