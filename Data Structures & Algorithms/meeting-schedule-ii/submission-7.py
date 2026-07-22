"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        i, j = 0, 0
        count, res = 0, 0

        while i < len(intervals):
            if starts[i] < ends[j]:
                i += 1
                count += 1
                res = max(res, count)
            else:
                j += 1
                count -= 1
        
        return res
