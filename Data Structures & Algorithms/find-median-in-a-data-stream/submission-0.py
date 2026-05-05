class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        min_heap = self.min_heap[:]
        max_heap = self.max_heap[:]

        while min_heap and max_heap:
            small = heapq.heappop(min_heap)
            big = -heapq.heappop(max_heap)

            if small == big:
                return small
            
            if small > big:
                return (small + big) / 2
                
        