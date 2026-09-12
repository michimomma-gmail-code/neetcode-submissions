class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

            return


        numcompo = 0
        for i in range(n):
            if i not in visit:
                numcompo += 1
            dfs(i, None)

        return numcompo

        