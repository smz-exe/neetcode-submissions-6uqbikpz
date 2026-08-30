class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)

        for weight in people:
            count[weight] += 1
        
        idx, weight = 0, 1
        while idx < len(people):
            while count[weight] == 0:
                weight += 1
            
            people[idx] = weight
            count[weight] -= 1
            idx += 1
        
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            res += 1
            remaining = limit - people[r]
            r -= 1

            if l <= r and remaining >= people[l]:
                l += 1
        return res
