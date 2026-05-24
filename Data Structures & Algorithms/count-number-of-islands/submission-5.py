from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        islands = 0

        def bfs(start_r: int, start_c: int) -> None:
            visited.add((start_r, start_c))
            q = deque([(start_r, start_c)])

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] == "1"
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands
