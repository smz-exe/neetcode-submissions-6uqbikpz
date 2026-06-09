class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        is_pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length <= 2:
                        is_pal[l][r] = True
                    else:
                        is_pal[l][r] = is_pal[l + 1][r - 1]

                if is_pal[l][r]:
                    count += 1
        
        return count