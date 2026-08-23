class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerical = ""

        for c in s:
            if (
                ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            ):
                alphanumerical += c
            elif ord("A") <= ord(c) <= ord("Z"):
                alphanumerical += chr((ord("a") + ord(c) - ord("A")))
        
        n = len(alphanumerical)
        for i in range(n // 2):
            if alphanumerical[i] != alphanumerical[n - 1 - i]:
                return False
        
        return True

        