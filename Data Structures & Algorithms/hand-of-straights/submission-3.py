import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counter = {}
        for num in hand:
            counter[num] = 1 + counter.get(num, 0)
        
        min_heap = list(counter.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                
                counter[i] -= 1
                if counter[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True
        
