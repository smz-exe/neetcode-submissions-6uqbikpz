class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_interval = res[-1]

            if start <= last_interval[1]:
                res[-1][1] = max(last_interval[1], end)
            else:
                res.append([start, end])
        
        return res
