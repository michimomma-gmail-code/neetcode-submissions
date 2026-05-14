class Solution:
    def climbStairs0(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

#        dp = [0] * (n + 1)
        prev = 1
        curr = 2

        for i in range(3, n + 1):
            #dp[i] = dp[i - 1] + dp[i - 2]
            prev, curr = curr, prev + curr
        
        return curr
