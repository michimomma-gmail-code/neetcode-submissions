class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] = True if dp[i-1] + nums[i] >= n
        # dp[0] = False
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i and dp[j]:
                    dp[i] = True

        return dp[n - 1]
        

