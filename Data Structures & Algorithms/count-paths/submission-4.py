class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            next_row = [1] * n

            for c in range(n - 2, -1, -1):
                next_row[c] = next_row[c + 1] + row[c]
            
            row = next_row
        
        return row[0]
