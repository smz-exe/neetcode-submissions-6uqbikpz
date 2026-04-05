class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            item = str(len(s)) + "_" + s
            res += item
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        num = ""
        i = 0
        while i < len(s):
            print(f"i={i}")
            if s[i] != "_":
                num += s[i]
                i += 1
            else:
                n = int(num)
                print(f"n={n}")
                num = ""
                item = ""
                for _ in range(n):
                    i += 1
                    item += s[i]
                res.append(item)
                print(f"item={item}")
                item = ""
                i += 1
        return res

