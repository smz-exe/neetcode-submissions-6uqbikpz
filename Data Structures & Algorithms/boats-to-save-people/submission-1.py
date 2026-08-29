class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)

        for w in people:
            count[w] += 1

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
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        
        return res