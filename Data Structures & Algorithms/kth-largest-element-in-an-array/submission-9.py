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
            
            if len(heap) == 1:
                return heap.pop()
            
            root = heap[0]
            heap[0] = heap.pop()

            i = 0
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right
                
                if smallest == i:
                    break
                
                heap[smallest], heap[i] = heap[i], heap[smallest]
                i = smallest
            
            return root
        
        for n in nums:
            push(-n)
        
        ans = 0
        for _ in range(k):
            ans = pop()
        
        return -ans
            

                















        for n in nums:
            heap.append(-n)
            i = len(heap) - 1

            while i > 0:
                parent = (i - 1) // 2

                if heap[parent] <= heap[i]:
                    break
                
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent


        root = heap[0]
        for _ in range(k):
            print(heap)
            root = heap[0]
            end = heap.pop()
            if heap:
                heap[0] = end
            else:
                heap.append(end)


            i = 0
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right
                
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return -root

                