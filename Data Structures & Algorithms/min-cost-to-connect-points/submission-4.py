class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append( (dist, i, j) )
                edges.append( (dist, j, i) )

        edges.sort()

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        cost = 0
        count = 0
        for dist, i, j in edges:
            if union(i, j):
                cost += dist
                count += 1

            if count == n - 1:
                break

        
        return cost
        
