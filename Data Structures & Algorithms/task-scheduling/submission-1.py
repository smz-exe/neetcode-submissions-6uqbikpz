class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        def counter(items: List[str]):
            counts = {}
            
            for x in items:
                counts[x] = 1 + counts.get(x, 0)
            
            return counts
        
        counts = counter(tasks)

        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time: # when the last idle time
                cnt, t = q.popleft()
                heapq.heappush(max_heap, cnt)
        
        return time

                