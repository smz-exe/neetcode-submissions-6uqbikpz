class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        type(Counter(s))
        return Counter(s) == Counter(t)