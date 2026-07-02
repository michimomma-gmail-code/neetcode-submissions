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