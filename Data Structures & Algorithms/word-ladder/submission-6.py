class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
#        wordList.append(endWord)

        def hasEdge(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                if count > 1:
                    return False
            return True

#        edge = []
        graph = [ [] for _ in range(len(wordList))]
        target_id = -1
        for i in range(len(wordList)):
            w1 = wordList[i]
            for j in range(i, len(wordList)):
                w2 = wordList[j]
                if hasEdge(w1, w2):
#                    edge.append( [i, j] )
                    graph[i].append(j)
                    graph[j].append(i)
            if w1 == endWord:
                target_id = i
        print(f'taret_id = {target_id}')
        if target_id == -1:
            return 0
        n = len(wordList)
        queue = deque( [n - 1] )

        visited = set()
        count = 0
        visited.add(n - 1)

        while queue:
            count += 1
#            print(f'count = {count}')
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == target_id:
#                    print(f'found: {wordList[i]}')
                    return count

                for nei in graph[i]:
                    if nei not in visited:
#                        print(f'testing {wordList[nei]}')
                        queue.append(nei)
                        visited.add(nei)
        return 0

            