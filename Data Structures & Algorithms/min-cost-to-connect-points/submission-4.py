import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        min_heap = [(0, 0)] # (cost, point)
        visited = set()
        res = 0

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            
            res += cost
            visited.add(point)

            for dist, nei in adj[point]:
                if nei in visited:
                    continue
                
                heapq.heappush(min_heap, (dist, nei))
        
        return res
        
        