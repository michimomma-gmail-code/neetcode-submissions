class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        queue = deque()

        num_fresh = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    queue.append( (r, c) )
                    
        if num_fresh == 0:
            return 0        

        delta = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] > 0:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            num_fresh -= 1
                            queue.append( (nr, nc) )

        
        if num_fresh > 0:
            return -1

        return(count -1)

                    
