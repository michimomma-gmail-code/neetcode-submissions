class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)

        if r1 == r2:
            return False

        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.parent[r1] = r2
            self.rank[r2] += self.rank[r1]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = []
        for i, (u, v, w) in enumerate(edges):
            sorted_edges.append( (i, u, v, w) )
        sorted_edges.sort(key=lambda x: x[3])

        def buildMST(block_idx = -1, force_idx = -1):
            uf = UnionFind(n)
            num_edges = 0
            sum_w = 0

            if force_idx > -1:
                u, v, w = edges[force_idx]
                uf.union(u, v)
                num_edges += 1
                sum_w += w

            for idx, u, v, w in sorted_edges:
                if (idx == force_idx) or (idx == block_idx):
                    continue

                if uf.union(u, v):
                    num_edges += 1
                    sum_w += w

            if num_edges == n - 1:
                return sum_w
        
            return float("infinity")

        m = len(edges)

        baseline_mst = buildMST()
        res_c = []
        res_p = []
        for i in range(m):
            mst = buildMST(block_idx = i)
            if mst > baseline_mst:
                res_c.append(i)
            else:
                mst_f = buildMST(force_idx = i)
                print(f'mst = {baseline_mst}, mst_f = {mst_f}')
                if mst_f == baseline_mst:
                    res_p.append(i)

        return [res_c, res_p]