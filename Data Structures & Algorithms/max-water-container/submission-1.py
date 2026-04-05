class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for l in range(n):
            for r in range(l, n):
                minh = min(heights[l], heights[r])
                width = r - l
                res = max(res, minh*width)
        return res
        