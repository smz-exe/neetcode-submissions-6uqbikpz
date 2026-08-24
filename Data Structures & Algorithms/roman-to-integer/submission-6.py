class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i, n = 0, len(s)
        while i < n:
            symbol = s[i]
            if symbol == "M":
                res += 1000
            elif symbol == "D":
                res += 500
            elif symbol == "C":
                if i + 1 < n and s[i + 1] == "M":
                    res += 900
                    i += 1
                elif i + 1 < n and s[i + 1] == "D":
                    res += 400
                    i += 1
                else:
                    res += 100
            elif symbol == "L":
                res += 50
            elif symbol == "X":
                if i + 1 < n and s[i + 1] == "C":
                    res += 90
                    i += 1
                elif i + 1 < n and s[i + 1] == "L":
                    res += 40
                    i += 1
                else:
                    res += 10
            elif symbol == "V":
                res += 5
            elif symbol == "I":
                if i + 1 < n and s[i + 1] == "X":
                    res += 9
                    i += 1
                elif i + 1 < n and s[i + 1] == "V":
                    res += 4
                    i += 1
                else:
                    res += 1
            print (i, res)
            i += 1
        
        return res
                