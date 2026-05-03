class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        def push(val: int) -> None:
            heap.append(val)
            i = len(heap) - 1

            while i > 0:
                parent = (i - 1) // 2

                if heap[parent] <= heap[i]:
                    break

                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent

        def pop() -> int:
            if not heap:
                raise IndexError("pop from empty heap")

            root = heap[0]
            last = heap.pop()

            if heap:
                heap[0] = last
                i = 0

                while True:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    smallest = i

                    if left < len(heap) and heap[left] < heap[smallest]:
                        smallest = left

                    if right < len(heap) and heap[right] < heap[smallest]:
                        smallest = right

                    if smallest == i:
                        break

                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest

            return root

        for x in nums:
            push(-x)

        ans = 0
        for _ in range(k):
            ans = pop()

        return -ans