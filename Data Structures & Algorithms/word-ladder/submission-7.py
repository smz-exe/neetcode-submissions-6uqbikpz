from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        
        word_set.add(beginWord)
        neighbors = defaultdict(list)

        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbors[pattern].append(word)
        
        visited = {beginWord}
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
    
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for nei_word in neighbors[pattern]:
                        if nei_word not in visited:
                            q.append(nei_word)
                    
                    neighbors[pattern] = []

            res += 1

        return 0
