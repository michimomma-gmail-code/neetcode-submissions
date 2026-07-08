class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # dp[m-1][n-1] = dp[m-1][n-2] + dp[m-2][n-1]

        dp = [ [1] * n  for _ in range(m)]
#        dp[0][0] = 1
#        print(dp)

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                row[c] = row[c] + row[c - 1]

        return row[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        row[0] = 1

        for _ in range(m):
            for c in range(1, n):
                row[c] += row[c - 1]

        return row[-1]