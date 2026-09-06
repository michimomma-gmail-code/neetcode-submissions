class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])

        def dfs(i, j):

            if (not 0 <= i < m) or (not 0 <= j < n):
                return 
            if grid[i][j] == "0":
                return 
            else:
                grid[i][j] = "0"

            for di, dj in delta:
                dfs(i + di, j + dj)
                    
            return 

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res