class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # dp[a] = min(dp[a], dp[a - coin] + 1)
        for coin in coins:
            for a in range(amount + 1):
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

#        print(dp)

        return dp[amount] if dp[amount] <= amount else -1
