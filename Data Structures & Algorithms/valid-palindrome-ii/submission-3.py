class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                s_left = s[l+1: r+1]
                s_right = s[l: r]
                return s_left == s_left[::-1] or s_right == s_right[::-1]
            
            l += 1
            r -= 1
        
        return True

                