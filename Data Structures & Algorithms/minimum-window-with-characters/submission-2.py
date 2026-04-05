class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapW = {}
        mapT = {}

        for c in t:
            mapT[c] = mapT.get(c, 0) + 1

        have, need = 0, len(mapT)
        l = 0
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            mapW[c] = mapW.get(c, 0) + 1

            if c in mapT and mapW[c] == mapT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                mapW[s[l]] -= 1
                if s[l] in mapT and mapW[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]: res[1]+1] if not res == [-1, -1] else ""



