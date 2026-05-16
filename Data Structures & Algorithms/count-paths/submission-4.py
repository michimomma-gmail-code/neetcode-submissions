class Solution:
    def uniquePaths0(self, m: int, n: int) -> int:
        dp = [ [1] * n for _ in range(m)]
#        dp[0][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = max(dp[r][c], dp[r - 1][c]+ dp[r][c - 1])

        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
#        dp = [ [1] * n for _ in range(m)]
#        dp[0][0] = 1
        dp2 = [1] * n

        for r in range(1, m):
            for c in range(1, n):
#                dp[r][c] = max(dp[r][c], dp[r - 1][c]+ dp[r][c - 1])
#                dp2[c] = max(dp2[c], dp2[c] + dp2[c - 1])
                dp2[c] = max(dp2[c], dp2[c] + dp2[c - 1])
                dp2
        return dp2[n - 1]
