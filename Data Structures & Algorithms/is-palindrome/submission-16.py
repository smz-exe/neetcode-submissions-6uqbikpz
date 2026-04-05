class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for c in s:
            if ("0"<= c <="9" or "A" <= c <= "Z" or "a" <= c <= "z"):
                formatted += c.lower()
        print(formatted)

        while len(formatted) > 1:
            if formatted[0] == formatted[-1]:
                formatted = formatted[1:-1]
                print(formatted)
            else:
                break
        
        return len(formatted) == 0 or len(formatted) == 1
            