class MedianFinder:
    # pattern: min-heap, max-heap
    # data structure: heap
    # main invariant: the difference of the length between small and large is less than and eaqual to 1
    # edge cases: 
    # time complexity: 
    # - addNum: O(log n)
    # - findMedian: O(1)

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2

        
        
        
        