class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

#        print(graph)
        visiting = set()
        visitingEdge = set()
        done = set()
        def dfs(node):
#            print(f'node = {node}')

            if node in done:
                return True

            if node in visiting:
                print(node, visiting)
                return False

            visiting.add(node)

            for nei in graph[node]:
#                print(f'nei = {nei}')
                n1, n2 = min(node, nei), max(node, nei)
                if (n1, n2) in visitingEdge:
                    continue
                else:
                    visitingEdge.add( (n1, n2))
                if not dfs(nei):
                    return False

            visiting.remove(node)
            done.add(node)

            return True

        # for node in list(graph.keys()):
        #     if not dfs(node):
        #         return False
        #     break
        node = edges[0][0]
        if not dfs(node):
            return False

        if len(done) < len(graph.keys()):
            return False
        return True