class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
#        cell2dist =  [[ -float("inf") for _ in range(n) ] for _ in range(n) ]
#        cell2dist[0][0] = grid[0][0]

        minheap = [ (grid[0][0], 0, 0) ] # (dist, x, y)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        done = set()

        while minheap:

            dist, x, y = heapq.heappop(minheap)

            if x == n - 1 and y == n - 1:
                return dist

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in done:
                    continue
                done.add((nx, ny))
                #ndist = grid[nx][ny]
                ndist = max(dist, grid[nx][ny])
                heapq.heappush(minheap, (ndist, nx, ny))


        return 0