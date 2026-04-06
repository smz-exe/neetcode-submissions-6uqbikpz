class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, h)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i - idx) * height)
                start = idx
            stack.append((start, h))

        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, (len(heights) - idx) * height)
        
        return maxArea