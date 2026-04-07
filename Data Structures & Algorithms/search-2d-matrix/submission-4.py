class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, b = 0, len(matrix) - 1

        while u <= b:
            mid = u + (b - u) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                u = mid + 1
        
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                r = m - 1
                 
        return False