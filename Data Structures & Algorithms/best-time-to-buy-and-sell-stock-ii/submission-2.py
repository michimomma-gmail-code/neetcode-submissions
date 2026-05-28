class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit: 
        # at i, buy (price i).
        #  or sell (price i - price j)
        #  or hold
        # dp[i] = max( price[i] - price[j], dp[i - 1] )
        #
        # [1, 2, 3, 4, 5]
        # dp[0] = 0
        # dp[1] = max( price[1] - price[0], dp[0])
        # dp[2] = max( price[2] - price[j], dp[1])
        n = len(prices) 
        dp = [0] * n

        for i in range(1, n):

            for j in range(i):
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j], dp[i - 1])

        print(dp)

        return max(dp)