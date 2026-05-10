class Solution:
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
