class Solution:
    def numSquares(self, n: int) -> int:
        # k*k <= n
        # k <= sqrt(n)
        # sum(k_i*k_i) = n
        #
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(n + 1):
            k = 1
#            for k in range(int(math.sqrt(n)) + 1):
            while k * k <= i:
                k2 = k * k
                if i - k2 >= 0:
                    dp[i] = min(dp[i - k2] + 1, dp[i])
                k += 1
        
#        print(dp)
        return dp[n]
