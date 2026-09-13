class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])

        #
        # node -> location: (i, j) 
        # distance -> max height
        #

        start = (0, 0)
        h = grid[0][0]
        minheap = []

        heapq.heappush(minheap, (h, start) )
        visited = set()

        while minheap:
            h, loc = heapq.heappop(minheap)
            if loc in visited:
                continue

            visited.add(loc)

            if loc == (m - 1, n - 1):
                return h

            for di, dj in delta:
                ni, nj = loc[0] + di, loc[1] + dj

                if not (0 <= ni < m) or not (0 <= nj < n):
                    continue

                heapq.heappush(minheap, ( max(h, grid[ni][nj]), (ni, nj) ) )


