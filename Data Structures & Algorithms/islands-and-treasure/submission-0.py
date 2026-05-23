from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None

        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def add_grid(r, c):
            out_of_bounds = r < 0 or c < 0 or r >= rows or c >= cols
            if (
                out_of_bounds
                or (r, c) in visited
                or grid[r][c] == -1
            ): 
                return
            
            visited.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
        
                add_grid(r + 1, c)
                add_grid(r - 1, c)
                add_grid(r, c + 1)
                add_grid(r, c - 1)
            
            dist += 1
