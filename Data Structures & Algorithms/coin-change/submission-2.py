class Solution:
    def coinChangeD(self, coins: List[int], amount: int) -> int:
        # 

        dp = [ (amount + 1) for _ in range(amount + 1)]
        # min number of coins to achive amount -- default is max with buffer (amount + 1)
        # dp[amount] <- min(dp[amount], dp[amount - coin] + 1)
        # base
        dp[0] = 0
#        dp[1] = dp[1 - 1] + 1 use 1 to achive amount

        for a in range(1, amount + 1):
            for c in coins:
                if a-c < 0:
                    continue
                dp[a] = min(dp[a], dp[a-c] + 1)


        return dp[amount] if dp[amount] <= amount else -1

    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        queue = deque( [0] ) #current amount

        seen = [False] * (amount + 1)
        seen[0] = True

        level = 0
        while queue:
            level += 1
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                for coin in coins:
                    temp = cur + coin
                    if temp == amount:
                        return level
                    
                    if temp > amount or seen[temp]:
                        continue

                    seen[temp] = True
                    queue.append( temp )


        return -1
