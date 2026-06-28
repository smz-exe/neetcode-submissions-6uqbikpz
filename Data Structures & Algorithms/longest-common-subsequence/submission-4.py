class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        cur = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            nxt = [0] * (m + 1)
            
            for c in range(m - 1, -1, -1):
                if text1[i] == text2[c]:
                    nxt[c] = 1 + cur[c + 1]
                else:
                    nxt[c] = max(nxt[c + 1], cur[c])
            
            cur = nxt
        
        return cur[0]
