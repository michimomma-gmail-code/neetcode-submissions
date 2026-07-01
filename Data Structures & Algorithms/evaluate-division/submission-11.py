class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.weight = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
            self.rank[x] = 1

    def find(self, x):
        if x not in self.parent:
            return None, -1
        orig_x = x
        weight = 1
        while self.parent[x] != x:
            weight *= self.weight[x]
            x = self.parent[x]
        self.weight[orig_x] = weight
        self.parent[orig_x] = x
        return self.parent[orig_x], self.weight[orig_x]

    def union(self, x, y, val):
        self.add(x)
        self.add(y)

        root_x, weight_x = self.find(x)
        root_y, weight_y = self.find(y)

        # x/y = val
        # x = weight_x * root_x
        # y = weight_y * root_y
        # weight_x * root_x / (weight_y * root_y) = val
        # root_x = weight_y / weight_x * val

        if self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
            self.weight[root_x] = (val * weight_y) / weight_x
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.weight[root_y] = weight_x / weight_y / val
            self.rank[root_x] += self.rank[root_y]

        


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

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind(len(equations))

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            uf.union(a, b, val)
#            uf.union(b, a, 1/val)

        res = []
        for a , b in queries:
            if a not in uf.parent or b not in uf.parent:
                res.append(-1)
                continue
            root_a, weight_a = uf.find(a)
            root_b, weight_b = uf.find(b)
            if root_a != root_b:
                res.append(-1)
            else:
                # weight_a = a / root, weight_b = b / root, 
                # a/b = weight_a / weight_b
                res.append(weight_a / weight_b)
        return res