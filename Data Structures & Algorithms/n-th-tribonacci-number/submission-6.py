class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0] * (n + 1)
#        dp[0], dp[1], dp[2] = 0, 1, 1

        def dfs(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1
            else:
                dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
                return dp[i]

        return dfs(n)
        
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

#        dp = [0] * (n + 1)

        dp_2 = 0
        dp_1 = 1
        dp_0 = 1
        for i in range(3, n + 1):
            dp = dp_2 + dp_1 + dp_0
            dp_2, dp_1, dp_0 = dp_1, dp_0, dp

        print(dp)
        return dp
