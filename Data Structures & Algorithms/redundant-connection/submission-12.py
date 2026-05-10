class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [ [] for _ in range(n + 1)]
        edge_s = {}
        for i, (u, v) in enumerate(edges):
            adj[u].append(v)
            adj[v].append(u)
            edge_s[(u, v)] = i
            edge_s[(v, u)] = i

        visiting = set()
        visited = []
        result = []

        def dfs(node, parent):

            if node in visiting:
                eg = (parent, node)
                maxid = edge_s[eg]
#                print(visited, eg)
#                print(maxid)
                while visited:
                    u, v = visited.pop()
                    if u == node or v == node:
                        break
                    if edge_s[(u, v)] > maxid:
                        maxid = edge_s[(u, v)]
                result.append(edges[maxid])
#                print(f'result = {result}')
                #print(node, visited)
                return False

            visiting.add(node)
            visited.append([parent, node])

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

#            print(f'done?')
            visiting.remove(node)
            visited.pop()

            return True

        dfs(n, None)

        return result[0]
