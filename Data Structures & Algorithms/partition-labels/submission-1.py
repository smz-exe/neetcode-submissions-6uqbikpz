class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_position: dict[str, int] = {}
        res = []

        for i in range(len(s)):
            last_position[s[i]] = i
        
        size = 0
        last_partition = 0
        for i in range(len(s)):
            size += 1
            last_partition = max(last_partition, last_position[s[i]])

            if i == last_partition:
                res.append(size)
                size = 0
        
        return res