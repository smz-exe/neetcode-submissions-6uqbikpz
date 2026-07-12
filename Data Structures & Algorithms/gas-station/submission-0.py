class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        def check(i: int) -> bool:
            store = 0
            for j in range(n):
                k = (i + j) % n
                store += gas[k]
                store -= cost[k]
                if store < 0:
                    return False
            
            return True
        
        for i in range(n):
            if check(i):
                return i
        
        return -1
