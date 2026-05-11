class Solution:
    def findRedundantConnection0(self, edges: List[List[int]]) -> List[int]:
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
        self.result = []
        done = set()

        def dfs(node, parent):
            if node in done:
                return True

            if node in visiting:
                eg = (parent, node)
                maxid = edge_s[eg]
#                print(visited, eg)
#                print(maxid)
                while visited:
                    u, v = visited.pop()
                    if edge_s[(u, v)] > maxid:
                        maxid = edge_s[(u, v)]
                    if u == node or v == node:
                        break
                self.result = edges[maxid]
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
            done.add(node)

            return True

        dfs(n, None)

        return self.result



    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        # parent array: parent[i] is the boss of i. Initially, everyone is their own boss.
        parent = [i for i in range(n + 1)]
        # rank array: used to keep the trees flat by attaching smaller trees under bigger ones
        rank = [1] * (n + 1)
        
        def find(node):
            # Follow the chain of bosses until we find the ultimate boss (where parent[node] == node)
            p = parent[node]
            while p != parent[p]:
                # "Path Compression": Point this node directly to its grandparent to speed up future lookups
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
            
        def union(n1, n2):
            boss1, boss2 = find(n1), find(n2)
            
            # If they have the same boss, they are already connected! We found the cycle.
            if boss1 == boss2:
                return False
                
            # Union by Rank: Attach the smaller company to the larger company
            if rank[boss1] > rank[boss2]:
                parent[boss2] = boss1
                rank[boss1] += rank[boss2]
            else:
                parent[boss1] = boss2
                rank[boss2] += rank[boss1]
                
            return True

        # Process the edges in the exact order they were given
        for u, v in edges:
            # The first edge that returns False from union() is our redundant connection
            if not union(u, v):
                return [u, v]


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [ i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def find(node):
            p = parent[node]

            while p != parent[p]:
                parent[parent[p]] = parent[parent[parent[p]]]
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(u, v):
            boss1 = find(u)
            boss2 = find(v)

            if boss1 == boss2:
                return False

            if rank[boss1] > rank[boss2]:
                parent[boss2] = boss1
                rank[boss2] += rank[boss1]
            else:
                parent[boss1] = boss2
                rank[boss1] += rank[boss2]

            return True


        for u, v in edges:
            if not union(u, v):
                return [u, v]

