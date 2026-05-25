class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pac, atl = set(), set()

        def dfs(r: int, c: int, visited: set[tuple[int, int]], prev_height) -> None:
            out_of_bounds = r < 0 or c < 0 or r >= rows or c >= cols

            if (
                out_of_bounds
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, -1)
            dfs(r, cols - 1, atl, -1)
        
        for c in range(cols):
            dfs(0, c, pac, -1)
            dfs(rows - 1, c, atl, -1)


        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res