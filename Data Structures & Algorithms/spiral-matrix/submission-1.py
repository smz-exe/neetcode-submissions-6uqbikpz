class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = 0, -1
        d = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = []
        left_steps = [len(matrix[0]), len(matrix) - 1]

        while left_steps[d & 1]:
            for i in range(left_steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])

            left_steps[d & 1] -= 1
            d += 1
            d %= 4
        
        return res