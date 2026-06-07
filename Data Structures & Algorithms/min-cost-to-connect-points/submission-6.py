class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        in_mst = [False] * n
        dist[0] = 0
        res = 0

        for _ in range(n):
            u = -1

            for v in range(n):
                if not in_mst[v] and (u == -1 or dist[v] < dist[u]):
                    u = v
            
            res += dist[u]
            in_mst[u] = True

            xu, yu = points[u]

            for v in range(n):
                if not in_mst[v]:
                    w = abs(xu - points[v][0]) + abs(yu - points[v][1])
                    if w < dist[v]:
                        dist[v] = w
        
        return res
