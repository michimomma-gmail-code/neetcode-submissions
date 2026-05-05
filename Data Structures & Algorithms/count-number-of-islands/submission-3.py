class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1] ]
        nrow = len(grid)
        ncol = len(grid[0])

        def dfs(r, c):


            if r < 0 or r >= nrow or c < 0 or c >= ncol or not grid[r][c] == "1":
                return 
            
            grid[r][c] = "#"

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return 

        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
    
        return res
