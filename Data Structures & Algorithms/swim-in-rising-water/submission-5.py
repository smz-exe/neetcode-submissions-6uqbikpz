class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        while min_heap:

            t, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:

                continue

            visited.add((r, c))

            if (r, c) == (n - 1, n - 1):

                return t

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:

                    heapq.heappush(

                        min_heap,

                        (max(t, grid[nr][nc]), nr, nc)

                    )

        return -1   