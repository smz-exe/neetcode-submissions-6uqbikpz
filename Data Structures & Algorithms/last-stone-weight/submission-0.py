class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            print(maxHeap)
            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)
            print(y, x)

            if y > x:
                heapq.heappush_max(maxHeap, y - x)
                print(y - x)
        
        return maxHeap[0] if len(maxHeap) > 0 else 0

