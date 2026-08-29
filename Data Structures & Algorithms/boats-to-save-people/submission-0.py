class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0

        while l < r:
            two_sum = people[l] + people[r]
            if two_sum > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            res += 1
        
        if l == r:
            res += 1
        
        return res
