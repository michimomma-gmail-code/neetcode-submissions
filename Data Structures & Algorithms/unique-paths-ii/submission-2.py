class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == n == 1:
            return 1 - obstacleGrid[0][0]

        dp = [ [0] * n for _ in range(m) ]

        for c in range(n - 1):
            if obstacleGrid[0][c] == 0:
                dp[0][c + 1] = 1
            else:
                break
        
        for r in range(m - 1):
            if obstacleGrid[r][0] == 0:
                dp[r + 1][0] = 1
            else:
                break


        print(dp)
        print(f'm = {m}, n = {n}')

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r - 1][c] == 1 and obstacleGrid[r][c - 1] == 1:
                    dp[r][c] = 0
                    continue

                if obstacleGrid[r - 1][c] == 0 and obstacleGrid[r][c - 1] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                elif obstacleGrid[r - 1][c] == 1:
                    dp[r][c] = dp[r][c - 1]
                elif obstacleGrid[r][c - 1] == 1:
                    dp[r][c] = dp[r - 1][c]

        
        return dp[m - 1][n - 1]