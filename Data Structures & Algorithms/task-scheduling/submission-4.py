class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for item in tasks:
            counts[item] = counts.get(item, 0) + 1
        
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            if cooldown and cooldown[0][1] <= time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(max_heap, cnt)
            
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1

                if cnt < 0:
                    cooldown.append((cnt, time + n + 1))
        
        return time



