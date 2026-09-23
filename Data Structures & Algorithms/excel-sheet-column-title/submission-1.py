class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        res = ""
        while num > 0:
            offset = (num - 1) % 26
            res += chr(ord("A") + offset)
            num = (num - 1) // 26
        
        return res[::-1]