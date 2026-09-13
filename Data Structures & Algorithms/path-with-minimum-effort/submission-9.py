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
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow = len(heights)
        ncol = len(heights[0])

        dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#        minheap = [(heights[0][0], 0, 0)]
        minheap = [(0, 0, 0)]

        r, c = 0, 0
        seen = set()
        while minheap:
#            print(minheap)

            max_h, r, c = heapq.heappop(minheap)

            if (r, c) in seen:
                continue
            seen.add( (r, c) )

            h = heights[r][c]

#            print(f'{r, c}, opt = {max_h}')

            if r == nrow -1 and c == ncol - 1:
#                print(seen)
                return max_h

            for dr, dc in dt:
                nxt_r, nxt_c = r + dr, c + dc
                if 0 <= nxt_r < nrow and 0 <= nxt_c < ncol and (nxt_r, nxt_c) not in seen:
                    dh = abs( heights[nxt_r][nxt_c] - h )
                    heapq.heappush(minheap, (max(max_h, dh), nxt_r, nxt_c ) )

        return 

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow = len(heights)
        ncol = len(heights[0])

        dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minheap = [ (0, 0, 0) ]
        r, c = 0, 0

        efforts = [ [float("infinity")] * ncol for _ in range(nrow)]

        while minheap:
#            print('minheap = ', minheap)
            max_h, r, c = heapq.heappop(minheap)
            if r == nrow - 1 and c == ncol - 1:
                return max_h
            
            if max_h > efforts[r][c]:
                continue
#            print(efforts)

            for dr, dc in dt:
                nxt_r, nxt_c = r + dr, c + dc
                if 0 <= nxt_r < nrow and 0 <= nxt_c < ncol:
                    dh = max(max_h, abs(heights[nxt_r][nxt_c] - heights[r][c]))
                    if dh < efforts[nxt_r][nxt_c]:
                        efforts[nxt_r][nxt_c] = dh
                        heapq.heappush(minheap, (dh, nxt_r, nxt_c))


    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        edges = []
        nrow = len(heights)
        ncol = len(heights[0])

        for r in range(nrow):
            for c in range(ncol):
                h = heights[r][c]
                if c < ncol - 1:
                    edges.append( ( abs(h - heights[r][c + 1]), r * ncol + c, r * ncol + c + 1 ) )
                if r < nrow - 1:
                    edges.append( ( abs(h - heights[r + 1][c]), r * ncol + c, (r + 1) * ncol +c ) )

#        print(edges)
#        print(sorted(edges, key=lambda x: x[1]))
        edges.sort()
        print(edges)

        uf = UnionFind(nrow * ncol)

        for w, u, v in edges:
            uf.union(u, v)
            if uf.find(0) == uf.find(nrow * ncol -1):
                return w
        return 0

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # generate graph

        m, n = len(heights), len(heights[0])            

#        adj = [ [] for _ in range(m * n) ]
        edge = []
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                h = heights[i][j]
                idx = i * n + j
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m) and (0 <= nj < n):
                        dh = abs(h - heights[ni][nj])
                        edge.append( (dh, idx, ni * n + nj ) )

        edge.sort()

        uf = UnionFind(m * n)
        res = 0
        for w, u, v in edge:
            uf.union(u, v)

            if uf.find(0) == uf.find(m * n - 1):
                return w

        return 0


































