class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        in_degree = { char: 0 for word in words for char in word }
        
        def extractEdge(w1, w2):

            l1 = len(w1)
            l2 = len(w2)
            
            for i in range(min(l1, l2)):
                if w1[i] == w2[i]:
                    continue
                else:
                    return (w1[i], w2[i])

            if w1 == w2[:l1]:
                if l1 > l2:
                    return None
                else:
                    return (w1, None)

        edges = set()
        for i in range( len(words) - 1 ):
            w1, w2 = words[i], words[i + 1]
            edge = extractEdge(w1, w2)
            if not edge:
                return ""
            elif not edge[1]:
                return edge[0]
            else:
                edges.add(edge)

        adj = defaultdict(list)
        for c1, c2 in edges:
            adj[c1].append(c2)
            in_degree[c2] += 1

        print(in_degree)
        queue = deque( [ char for char in in_degree if in_degree[char] == 0 ] )
        print(adj)
        print(queue)

        res = []
        while queue:

            char = queue.popleft()
            res.append(char)

            for nchar in adj[char]:
                in_degree[nchar] -= 1
                if in_degree[nchar] == 0:
                    queue.append( nchar )

        for v in in_degree.values():
            if v > 0:
                return ""

        if res:
            return "".join(res)
        else:
            return ""
