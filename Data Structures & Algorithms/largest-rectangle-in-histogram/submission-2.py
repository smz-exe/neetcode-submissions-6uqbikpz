class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (i, h)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popIdx, popHeight = stack.pop()
                maxArea = max(maxArea, (i - popIdx) * popHeight)
                start = popIdx
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea