class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                    dfs(nei)
                else:
                    visited.add(nei)
            
            if node not in visited:
                return True
            else:
                return False

        count = 0
        for node in adj:
            print(f'node = {node}')
            if dfs(node):
                count += 1
        
        return count




















    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
