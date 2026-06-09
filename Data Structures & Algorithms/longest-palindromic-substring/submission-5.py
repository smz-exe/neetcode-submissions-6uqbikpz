class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        res = ""
        max_len = 0

        for i in range(1, n + 1):
            for l in range(n - i + 1):
                r = l + i - 1

                if i == 1:
                    is_pal[l][r] = True
                elif i == 2:
                    if s[l] == s[r]:
                        is_pal[l][r] = True
                else:
                    if s[l] == s[r]:
                        is_pal[l][r] = is_pal[l + 1][r - 1]
                
                if is_pal[l][r] and i > max_len:
                    max_len = i
                    res = s[l: r + 1]
        
        return res

                    