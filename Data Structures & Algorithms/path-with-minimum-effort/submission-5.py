class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]

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

        # starting from st: (r, c) to (r + dr, c + dc)
        # distance = |heights[r + dr][c + dc] - heights[r][c]|
        #
        # [1, 1, 1]
        # [3, 2, 4]
        # [2, 5, 4]
        #
        # [[1], 1, 1] q = { (0, (0,0)) }
        # [3, 2, 4]
        # [2, 5, 4]
        #
        # [[1], [1], 1] q = { (2, (1, 0)), (0, (0, 1)) }
        # [<3>, 2, 4]
        # [2, 5, 4]
        #
        # [[1], [1], [1]] q = { (2, (1, 0)), (0, (0,2)), (1, (1,1)) }
        # [<3>,  [2],  4]
        # [2,    5,  4]
        #
        # [[1], [1], [1]] q = { (2, (1, 0)), (1, (1,1)) , (3, (1, 2))}
        # [<3>,  [2],  [4]]
        # [2,    5,  4]
        #
        # [[1], [1], [1]] q = { (2, (1, 0)), x(1, (1,1)) , (3, (1, 2)), (2, (2,1))}
        # [<3>,  [2],  <4>]
        # [2,    [5],  4]

        # for each (r + dr, c + dc)
        # compute min ( hights[r+dr][c+dc] - hights[r][c], )
        # 