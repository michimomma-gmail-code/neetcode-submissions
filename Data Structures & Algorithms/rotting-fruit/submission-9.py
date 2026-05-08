class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        queue = deque()
        selected = set()

        count1 = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    count1 += 1
                if grid[r][c] == 2:
                    queue.append( (r, c) )
                    selected.add( (r, c) )
        if count1 == 0:
            return 0
    
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # if grid[r][c] == 1:
                #     grid[r][c] = 2
                #     count1 -= 1

                for dr, dc in delta:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < nrow and 0 <= nc < ncol) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append( (nr, nc) )
                        count1 -= 1

        if count1 != 0:
            return -1

        return(count - 1)