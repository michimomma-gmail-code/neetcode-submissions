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
#        visitingEdge = set()
#        done = set()

        def dfs(node, parent):
#            print(f'node = {node}')

#            if node in done:
#                return True

            if node in visiting:
#                print(node, visiting)
                return False

            visiting.add(node)

            for nei in graph[node]:

                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

#            visiting.remove(node)
#            done.add(node)

            return True

        if not dfs(0, -1):
            return False

        return len(visiting) == n
