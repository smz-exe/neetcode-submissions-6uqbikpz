import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q_to_len: dict[int, int] = {}
        min_heap = []
        i = 0
        
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            q_to_len[q] = min_heap[0][0] if min_heap else -1
        
        return [q_to_len[q] for q in queries]
