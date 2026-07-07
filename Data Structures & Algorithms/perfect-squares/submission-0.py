class Solution:
    def numSquares(self, n: int) -> int:
        # k*k <= n, k <= sqrt(n)
        # 1x1, 2*2, 3*3 <= 13
        # 
        dp = [n] * (n + 1) # # perfect numbers that sum to i
        dp[0] = 0
        dp[1] = 1
        #
        for i in range(1, n + 1):
#            print(int(math.sqrt(i)))
            for k in range(1, int(math.sqrt(i)) + 1):
                k2 = k * k
                if i - k2 >= 0:
                    #print(i, dp[i], dp[i - k2] + 1)
                    dp[i] = min(dp[i], dp[i - k2] + 1)
        
        print(dp)
        return dp[n]