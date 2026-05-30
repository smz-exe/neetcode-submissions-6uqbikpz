from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        max_area = 0

        def bfs(start_r: int, start_c: int) -> int:
            q = deque()
            visited.add((start_r, start_c))
            q.append((start_r, start_c))
            area = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
                        print(f"area updated: {area} ")
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area

