class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        return res
            