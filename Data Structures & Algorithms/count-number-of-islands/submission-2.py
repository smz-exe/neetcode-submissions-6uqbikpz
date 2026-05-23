from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        islands = 0

        def bfs(r: int, c: int) -> None:
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    is_in = nr >= 0 and nc >=0 and nr < rows and nc < cols
                    if (
                        is_in
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands