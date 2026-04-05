class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashmap = {}
        longest = 0
        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
                r += 1
            else:
                longest = max(longest, r - l)
                nl = hashmap[s[r]] + 1
                for i in range(l, nl):
                    print(s[i])
                    print(hashmap[s[i]])
                    del hashmap[s[i]]
                l = nl
                hashmap[s[r]] = r
                r += 1
        else:
            longest = max(longest, r - l)
        return longest
        
