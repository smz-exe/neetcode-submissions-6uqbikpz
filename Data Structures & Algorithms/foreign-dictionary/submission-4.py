class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]
            common_len  = min(len(first_word), len(second_word))

            if (
                len(first_word) > len(second_word)
                and first_word[:common_len] == second_word[:common_len]
            ):
                return ""

            for j in range(common_len):
                if first_word[j] != second_word[j]:
                    before_char = first_word[j]
                    after_char = second_word[j]
                    graph[before_char].add(after_char)
                    break
        
        NOT_VISITED = 0
        VISITING = 1
        VISITED = 2
        state = {char: NOT_VISITED for char in graph}
        reverse_order = []

        def has_cycle(char: str) -> bool:
            if state[char] == VISITING:
                return True
            
            if state[char] == VISITED:
                return False
            
            state[char] = VISITING
            
            for next_char in graph[char]:
                if has_cycle(next_char):
                    return False
            
            state[char] = VISITED
            reverse_order.append(char)
            return False
        
        for char in graph:
            if has_cycle(char):
                return ""
        
        return "".join(reversed(reverse_order))
            
            
            
