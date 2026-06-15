class Solution:
    def countComponents0(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print(adj)

        visited = set()
        def dfs(node):
            for nei in adj[node]:
                print(f'nei = {nei}')
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)            
            return

        count = 0
        for i in range(len(adj)):
            if i not in visited:
                dfs(i)
                count += 1
                
        
        return count


    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]

        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return 0

            parent[root1] = root2
            return 1

        num_component = n

        for u, v in edges:
            if union(u, v) == 1:
                num_component -= 1

        return num_component
        










    def countComponents1(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            return

        count = 0
        for i in range(n):
            if not i in visited:
                dfs(i)
                count += 1
        
        return count
