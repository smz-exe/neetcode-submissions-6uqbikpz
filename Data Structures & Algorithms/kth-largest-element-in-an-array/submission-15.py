class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def __len__(self) -> int:
        return len(self.heap)
        
    def push(self, val: int) -> None:
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sift_down(0)
        return root
    
    def peek(self) -> int:
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break
            
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
    
    def _sift_down(self, i: int) -> None:
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
            
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()

        for n in nums:
            heap.push(n)
            if len(heap) > k:
                heap.pop()
        
        return heap.peek()
        