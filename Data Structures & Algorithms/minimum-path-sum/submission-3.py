class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#
        m, n = len(grid), len(grid[0])
        dp = grid
        for r in range(1, m):
            dp[r][0] += dp[r - 1][0]
        for c in range(1, n):
            dp[0][c] += dp[0][c - 1]

        for r in range(1, m):
            for c in range(1, n):
                temp_c, temp_r  = dp[r][c - 1], dp[r - 1][c]
                dp[r][c] += min(temp_c, temp_r)

        return dp[m - 1][n - 1]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
#
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for c in range(1, n):
            dp[c] += grid[0][c] + dp[c - 1]
        
#        print(dp)
        for r in range(1, m):
            for c in range(0, n):
                if c > 0:
                    dp[c] = min(dp[c - 1], dp[c]) + grid[r][c]
                else:
                    dp[c] += grid[r][c]

        return dp[n - 1]
