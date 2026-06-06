import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj: list[tuple[int, int]] = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
            
        res = 0
        visited = set()
        min_heap = [(0, 0)] # cost, point

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            visited.add(i)
            res += cost
            
            for nei_cost, nei in adj[i]:
                if nei in visited:
                    continue
                
                heapq.heappush(min_heap, (nei_cost, nei))
        
        return res

