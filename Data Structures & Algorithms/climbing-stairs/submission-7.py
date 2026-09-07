class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[n] = dp[n - 1] + dp[n - 2]
        # dp dp_1, dp_2
        dp_1, dp_2 = 1, 1
        dp = 1
        for i in range(1, n):
            dp = dp_1 + dp_2
            dp_1, dp_2 = dp, dp_1

        return dp
        