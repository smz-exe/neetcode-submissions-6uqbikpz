class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for p in points:
            x, y = p
            dis = x*x + y*y
            heapq.heappush(minHeap, (-dis, p))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for n_dis, p in minHeap:
            res.append(p)
        return res