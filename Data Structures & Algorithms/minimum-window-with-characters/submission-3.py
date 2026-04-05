class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countW, countT = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            countW[c] = countW.get(c, 0) + 1
            
            if c in countT and countW[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        
        return s[res[0]:res[1] + 1] if res is not [-1, -1] else ""




