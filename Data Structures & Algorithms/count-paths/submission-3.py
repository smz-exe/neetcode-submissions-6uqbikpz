class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * (n + 1)

        for _ in range(m - 1):
            next_row = [0] * (n + 1)

            for c in range(n - 1, -1, -1):
                next_row[c] = next_row[c + 1] + row[c]
            
            row = next_row
        
        return row[0]
