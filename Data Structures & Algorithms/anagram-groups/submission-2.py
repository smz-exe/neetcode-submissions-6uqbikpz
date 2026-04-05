class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for s in strs:
            key = ''.join(sorted(s))
            buckets.setdefault(key, []).append(s)
        
        groups = []
        for value in buckets.values():
            groups.append(value)
        return groups