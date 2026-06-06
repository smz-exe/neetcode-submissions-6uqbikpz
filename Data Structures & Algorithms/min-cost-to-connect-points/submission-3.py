import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)] # (dist, point)
        res = 0

        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue
            
            res += cost
            visited.add(i)
            for dist, nei in adj[i]:
                if nei in visited:
                    continue
                heapq.heappush(min_heap, (dist, nei))
        
        return res