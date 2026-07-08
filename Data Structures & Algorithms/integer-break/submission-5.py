class Solution:
    def integerBreak(self, n: int) -> int:
        # n = 12
        # 12/2 = 6 6x2 6x6=36
        # 12/3 = 4 4x3 4x4x4=64
        # 12/4 = 3 3x4 3x3x3x3=81
        # 12/6 = 2 2x6 2x2x2x2x2x2=64 


        # 1
        # 2: 1x1 = 1
        # 3: 2x1 = 1
        # 4: 3x1 = 3, 2x2 = 4
        # 5: 3x2 = 6
        # 6: 2x2x2 = 8, 3x3 = 9
        # 7
        # 8: 2x2x2x2 = 8, 4x4=16
        # 9: 3x3 = 9
        # 10: 2x2x2x2x2 = 32, 5x5=25
        # 11:
        # 12: 2x2x2x2x2x2 = 64, 3x3x3x3=81, 4x4x4=64, 6x6=36

        dp = [0] *  (n + 1)
#
        dp[0] = 0
        dp[1] = 1
#        dp[2] = 2
#        dp[3] = 3
        for i in range(2, n + 1):
            for m in range(1, i + 1):
                if i >= m:
                    dp[i] = max(dp[i - m] * m, (i - m ) * m, dp[i])

        print(dp)
        return dp[n]

