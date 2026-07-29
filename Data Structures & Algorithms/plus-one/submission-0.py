class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        res = []

        for i in range(len(digits) - 1, -1, -1):
            d = digits[i] + c
            c = d // 10
            d %= 10
            res.append(d)
        
        if c:
            res.append(c)
        
        return [res[i] for i in range(len(res) - 1, -1, -1)]