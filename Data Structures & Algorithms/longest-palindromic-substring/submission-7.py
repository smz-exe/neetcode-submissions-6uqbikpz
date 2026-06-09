class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        res = ""
        max_len = 0

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length <= 2:
                        is_pal[l][r] = True
                    else:
                        is_pal[l][r] = is_pal[l + 1][r - 1]
                
                if is_pal[l][r] and length > max_len:
                    max_len = length
                    res = s[l: r + 1]
        
        return res
