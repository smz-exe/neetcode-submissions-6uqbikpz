class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cand = strs[0]

        for s in strs[1:]:
            for i in range(len(cand)):
                if i >= len(s) or cand[i] != s[i]:
                    cand = cand[:i]
                    break
                
        return cand