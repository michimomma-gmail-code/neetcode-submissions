class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [False] * (amount + 1)
        cnt = [0] * (amount + 1)

        dp[0] = True
        cnt[0] = 1
        
        for coin in coins:
            for a in range(coin, amount + 1):
#                print(f'a = {a}, coin = {coin}')
                if a - coin >= 0 and dp[a - coin]:
                    dp[a] = True
                    cnt[a] += cnt[a - coin]
        print(cnt)
        return cnt[amount]