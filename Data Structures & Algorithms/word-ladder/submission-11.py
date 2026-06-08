from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        
        word_set.add(beginWord)
        pattern_dict = defaultdict(set)

        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_dict[pattern].add(word)
    
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

                    for nei in pattern_dict[pattern]:
                        if nei in visited:
                            continue
                        
                        visited.add(nei)
                        q.append(nei)
            
            steps += 1
        
        return 0

