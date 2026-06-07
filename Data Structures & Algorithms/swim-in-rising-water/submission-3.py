import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        min_heap = [(grid[0][0], (0, 0))]
        visited = set((0, 0))

        while min_heap:
            t, (r, c) = heapq.heappop(min_heap)

            if (r, c) == (n - 1, n - 1):
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                out_of_bounds = nr < 0 or nc < 0 or nr >= n or nc >= n

                if (
                    out_of_bounds
                    or (nr, nc) in visited
                ):
                    continue
                
                visited.add((nr, nc))
                heapq.heappush(min_heap, (max(t, grid[nr][nc]), (nr, nc)))
        
        return -1