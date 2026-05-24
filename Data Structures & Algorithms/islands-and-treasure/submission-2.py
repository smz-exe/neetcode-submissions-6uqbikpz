from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        INF = 2147483647

        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def add_cell(r: int, c: int) -> None:
            out_of_bounds = r < 0 or c < 0 or r >= rows or c >= cols
            if (
                out_of_bounds
                or grid[r][c] != INF
                or (r, c) in visited
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
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    add_cell(r + dr, c + dc)

            dist += 1
        
