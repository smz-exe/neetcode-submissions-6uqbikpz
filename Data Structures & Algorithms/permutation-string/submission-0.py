class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS1 > lenS2:
            return False

        sortedS1 = sorted(s1)
        for i in range(lenS2 - lenS1 + 1):
            subS2 = s2[i:i+lenS1]
            sortedSubS2 = sorted(subS2)
            if (sortedS1 == sortedSubS2):
                return True
        else:
            return False
        
