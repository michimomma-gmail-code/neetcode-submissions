class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(dict)

        for i in range(n):
            a, b = equations[i]
            val = values[i]
            adj[a][b] = val
            adj[b][a] = 1 / val

        def dfs(node, target):
            if node not in adj:
                return -1

            if node == target:
                return 1

            seen.add(node)

            for nxt_node, val in adj[node].items():
                if nxt_node not in seen:
#                    seen.add( nxt_node )
                    temp = dfs(nxt_node, target)
                    if temp == -1:
                        continue
                    return temp * val
        
            return -1


        output = []
        for a, b in queries:
            seen = set()
            output.append( dfs(a, b) )

        return output