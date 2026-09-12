class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

#        print(graph)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                dfs(nei)

            return


        numcompo = 0
        for i in range(n):
            if i not in visit:
                numcompo += 1
            dfs(i)

        return numcompo



    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        print(parent)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        connected = n
        for u, v in edges:
            if union(u, v):
                connected -= 1

        return connected