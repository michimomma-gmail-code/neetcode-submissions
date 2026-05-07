class Solution:
    def islandsAndTreasure0(self, grid: List[List[int]]) -> None:
        
        nrow, ncol = len(grid), len(grid[0])
        inf = 2147483647

        def bfs(r, c):

            queue = deque( [(r, c)] )
            level = 0
            visited = set()
            while queue:
                found = False
                lq = len(queue)
                for i in range(lq):
                    _r, _c = queue.popleft()
                    if (_r, _c) in visited:
                        continue
                    else:
                        visited.add( (_r, _c) )

                    if not 0 <= _r < nrow or not 0 <= _c < ncol:
                        continue
                    if grid[_r][_c] == -1:
                        continue

                    if grid[_r][_c] == 0:
#                        print(_r, _c)
                        found = True
                        #break
                    queue.append( (_r, _c - 1) )
                    queue.append( (_r, _c + 1) )
                    queue.append( (_r - 1, _c) )
                    queue.append( (_r + 1, _c) )

                if found:
                    break
                level += 1

            return level

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r,c)

    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrow, ncol = len(grid), len(grid[0])
        inf = 2147483647

        queue = deque()
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    queue.append( (r, c) )

        
        while queue:

            r, c = queue.popleft()

            for dr, dc in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
                _r = r + dr
                _c = c + dc

                if 0 <= _r < nrow and 0 <= _c < ncol and grid[_r][_c] == inf:
                    grid[_r][_c] = grid[r][c] + 1
                    queue.append( (_r, _c) )

        