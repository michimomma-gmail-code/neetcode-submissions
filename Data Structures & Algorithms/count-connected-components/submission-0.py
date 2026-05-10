class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
            
            return True

        count = 0
        for i in range(n):
            if dfs(i, None):
                count += 1
        
        return count
