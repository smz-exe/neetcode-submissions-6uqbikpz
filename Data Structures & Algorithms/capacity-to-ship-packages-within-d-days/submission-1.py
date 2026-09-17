class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def can_ship(cap: int) -> bool:
            ships, curr_cap = 1, cap
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr_cap = cap
                
                curr_cap -= w
            return True
        
        while l <= r:
            cap = l + (r - l) // 2
            if can_ship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res