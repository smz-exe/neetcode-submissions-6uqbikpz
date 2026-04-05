class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(type(Counter(s)))
        return Counter(s) == Counter(t)