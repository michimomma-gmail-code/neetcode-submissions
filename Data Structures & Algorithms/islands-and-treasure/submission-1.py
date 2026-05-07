class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
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

    