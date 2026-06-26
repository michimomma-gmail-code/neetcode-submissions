class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(dict)

        for i in range(n):
            a, b = equations[i]
            val = values[i]
            adj[a][b] = val
            adj[b][a] = 1 / val

#        print(adj)

        #reachable

        def dfs(node, cur_val):
            reachable = {node: cur_val }
            # if node not in adj:
            #     return
#            print(adj[node].items())
            for nxt_node, val in adj[node].items():
#                print(f'nxt node = {nxt_node}, val = {val}')
                if (nxt_node not in seen):# and (nxt_node != node):
                    seen.add( nxt_node )
                    temp = dfs(nxt_node, cur_val * val)
#                    print(temp)
                    reachable.update( temp )

            return reachable

        res = defaultdict(dict)
        for node in adj:
            seen = set()
            res[node].update( dfs(node, 1) )

        output = []
        for a, b in queries:
            if a in res and b in res[a]:
                output.append(res[a][b])
            else:
                output.append(-1)

        return output