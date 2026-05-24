from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        t = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for _ in range(len(q)):

                r, c = q.popleft()
                print(f"poped: ({r}, {c})")

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        print(f"checked ({nr}, {nc})")
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                print("done 4 directions")
            print(f"current time: {t}\n")
            t += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return t - 1 if t > 0 else 0


