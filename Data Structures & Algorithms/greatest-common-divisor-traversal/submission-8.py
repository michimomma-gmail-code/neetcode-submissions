class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
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

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        uf = UnionFind(n)
        if n == 1:
            return True

        first_fac_num = {} # fac: index
        for i, num in enumerate(nums):
        
            fac = 2

            while fac * fac <= num:
                if num % fac == 0:
                    if fac in first_fac_num:
                        uf.union(i, first_fac_num[fac])
                    else:
                        first_fac_num[fac] = i
#                        print(f'num = {num}, adding {fac}')

                    while num % fac == 0:
                        num //= fac
                fac += 1
            
            if num > 1:
                if num in first_fac_num:
                    uf.union(i, first_fac_num[num])
                else:
#                    print(f'num = {num}, adding {num}')
                    first_fac_num[num] = i

#        print(first_fac_num)
        r0 = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != r0:
                return False
        return True




