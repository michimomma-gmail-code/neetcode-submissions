class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        queue = deque()
        selected = set()

        count1 = 0
        count2 = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    count1 += 1
                if grid[r][c] == 2:
                    queue.append( (r, c) )
                    count2 += 1
        if count1 == 0:
            return 0
    
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    count1 -= 1

                for dr, dc in delta:
                    if not (0 <= r + dr < nrow and 0 <= c + dc < ncol) or grid[r + dr][c + dc] == 0:
                        continue
                    if grid[r + dr][c + dc] == 1 and (r + dr, c + dc) not in selected:
                        queue.append( (r + dr, c + dc) )
                        selected.add( (r + dr, c + dc) )
            print(f'num q = {len(queue)}')

        if count1 != 0:
            return -1

        return(count - 1)