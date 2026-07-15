class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index: dict[str, int] = {}
        res = []

        for i in range(len(s)):
            last_index[s[i]] = i
        
        size = 0
        r = 0
        for i in range(len(s)):
            size += 1
            r = max(r, last_index[s[i]])

            if i == r:
                res.append(size)
                size = 0
        
        return res