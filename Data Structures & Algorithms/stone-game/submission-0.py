class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # at step i, take either piles[l] or piles[r]
        # l += 1, r -= 1
        n = len(piles)
        l, r = 0, n - 1

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            if piles[l] > piles[r]:
                dp[i] = piles[l] - dp[i + 1]
                l += 1
            else:
                dp[i] = piles[r] - dp[i + 1]
                r -= 1

        print(dp)
        if dp[n - 1] > 0:
            return True
        else:
            return False

            