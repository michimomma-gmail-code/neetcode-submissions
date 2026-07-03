class UnionFind:
    def __init__(self, n):
        self.parent = {}
    def add(self, node):
        if node not in self.parent:        
            self.parent[node] = node
    def find(self, node):
        if node not in self.parent:
            return node
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        self.parent[root2] = root1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        uf = UnionFind(n)
        edges = {}

        for i in range(n):
            num_i = nums[i]
            for j in range(i + 1, n):
                num_j = nums[j]
                if math.gcd(num_i, num_j) > 1:
                    edges[(num_i, num_j)] = 1
                    edges[(num_j, num_i)] = 1

        if not edges:
            return False
        for u, v in edges:
            uf.add(u)
            uf.add(v)
            uf.union(u, v)

        print(edges)
        print(uf.parent)
        r0 = uf.find(nums[0])
        for i in range(1, n):
            ri = uf.find(nums[i])
            if ri != r0:
                return False
        return True
