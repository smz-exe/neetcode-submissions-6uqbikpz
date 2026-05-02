class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for p in points:
            x, y = p
            dis = x*x + y*y
            heapq.heappush(minHeap, (dis, p))
        
        print(minHeap)
        res = []
        for i in range(k):
            dis, p = heapq.heappop(minHeap)
            res.append(p)
        
        return res