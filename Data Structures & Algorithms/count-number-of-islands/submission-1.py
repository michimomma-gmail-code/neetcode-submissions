class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])

        def dfs(r, c):

            result = False

            if r < 0 or r >= nrow or c < 0 or c >= ncol or not grid[r][c] == "1":
                return result
            
            grid[r][c] = "#"
            result = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
            return result

        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
    
        return res
