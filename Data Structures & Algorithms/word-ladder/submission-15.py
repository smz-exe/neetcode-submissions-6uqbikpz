from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        
        word_set.add(beginWord)
        pattern_to_words = defaultdict(list)

        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_to_words[pattern].append(word)
    
        visited = {beginWord}
        q = deque([beginWord])
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for next_word in pattern_to_words.pop(pattern, []):
                        if next_word not in visited:
                            visited.add(next_word)
                            q.append(next_word)
            
            steps += 1
        
        return 0
