class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temp, index)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t, i))
        
        return res


