class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # min(abs(x + y), abs(x - y))
        #
        # dp: index - sum(stones)
        # dp[i]: sum(stone) = i
        #
        # dp[0]: 0
        # dp[1]: (2 - 1)
        # dp[2]: 1+dp[1], 3-dp[1]
        total = sum(stones)
        target = total // 2

        dp = [float("infinity")] * (target + 1)
        dp[0] = 0
#        num_s = len(stones)
#        for j in range(num_s):
        for stone in stones:
            for i in range(len(dp) - 1, -1, -1):
                if i - stone >= 0:
                    dp[i] = min(dp[i], dp[i - stone] + stone)
        
        print(dp)
        i = target
        while dp[i] == float("infinity"):
            i -= 1
        total_pos = dp[i]
        total_neg = total - total_pos

        return abs(total_pos - total_neg)
