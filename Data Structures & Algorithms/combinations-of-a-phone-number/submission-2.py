class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dig_to_char = {"2": ("a", "b", "c"),
                        "3": ("d", "e", "f"),
                        "4": ("g", "h", "i"),
                        "5": ("j", "k", "l"),
                        "6": ("m", "n", "o"), 
                        "7": ("p", "q", "r", "s"),
                        "8": ("t", "u", "v"),
                        "9": ("w", "x", "y", "z")}
        

        def dfs(i: int) -> None:
            print("called", i)
            if i == len(digits):
                return [""]
            combs = dfs(i + 1)
            print("returned from", i - 1)
            print(combs)
            res = []
            chars = dig_to_char[digits[i]]
            print(chars)
            for c in chars:
                print(c)
                for comb in combs:
                    print(comb, "comb")
                    res.append(c + comb)
            return res
        
        return dfs(0)