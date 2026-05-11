class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
#        wordList.append(endWord)
        patterns = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patterns[pattern].append(word)


        n = len(wordList)
        queue = deque( [beginWord] )

        visited = set()
        count = 0
        visited.add( beginWord )

        while queue:
            count += 1
#            print(f'count = {count}')
            for _ in range(len(queue)):
                w = queue.popleft()

                if w == endWord:
                    return count

                for j in range(len(w)):
                    ptn = w[:j] + "*" + w[j+1:]
#                    print(f'{ptn} patterns = {patterns[ptn]}')

                    for nei in patterns[ptn]:
#                        print(f'nei = {nei}')

                        if nei not in visited:
#                            print(f'adding {nei}')
                            queue.append(nei)
                            visited.add(nei)


        return 0

            