class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#        dp[r][c] = dp[r][c -1] + dp[r - 1][c]
#
        m, n = len(grid), len(grid[0])
 #       dp = [ [0] * n for _ in range(m) ]
#        dp[0][0] = grid[0][0]
        dp = grid

        for r in range(m):
            for c in range(n):
#                temp_c = temp_r = grid[r][c]
                if c == 0 and r == 0:
                    continue

                if c > 0 and r > 0:
                    temp_c, temp_r  = dp[r][c - 1], dp[r - 1][c]
                    dp[r][c] += min(temp_c, temp_r)
                elif c == 0:
                    dp[r][c] += dp[r - 1][c]
                elif r == 0:
                    dp[r][c] += dp[r][c - 1]

#            print(dp)

        return dp[m - 1][n - 1]
    
