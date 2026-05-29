class Solution:
    def maxProfit0(self, prices: List[int]) -> int:
        # profit: 
        # at i, buy (price i).
        #  or sell (price i - price j)
        #  or hold
        # dp[i] = max( price[i] - price[j], dp[i - 1] )
        #
        # [1, 2, 3, 4, 5]
        # dp[0] = 0
        # dp[1] = max( dp[j] + price[1] - price[0], dp[0])
        # dp[2] = max( dp[j] + price[2] - price[j], dp[1])
        n = len(prices) 
        dp = [0] * n

        for i in range(1, n):

            for j in range(i):
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j], dp[i - 1])

        print(dp)

        return max(dp)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices) == 1:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)

        return profit

#    def maxProfit(1self, prices: List[int]) -> int:
# hold  
