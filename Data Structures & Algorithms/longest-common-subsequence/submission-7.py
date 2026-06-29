class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        below = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            current = [0] * (m + 1)

            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = 1 + below[j + 1]
                else:
                    current[j] = max(current[j + 1], below[j])
            
            below = current
        
        return below[0]