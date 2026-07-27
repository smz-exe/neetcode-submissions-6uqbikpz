class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n

        while cur not in seen:
            if cur == 1:
                return True
            
            seen.add(cur)
            
            sum = 0
            while cur > 0:
                d = cur % 10
                sum += d*d
                cur //= 10
            
            cur = sum
        
        return False
        