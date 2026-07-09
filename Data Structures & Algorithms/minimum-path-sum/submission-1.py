class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#        dp[r][c] = dp[r][c -1] + dp[r - 1][c]
#
        m, n = len(grid), len(grid[0])
 #       dp = [ [0] * n for _ in range(m) ]
#        dp[0][0] = grid[0][0]
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
    
