class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = 1, dp[0] = nums[0]
        # n = 2, dp[1] = max(nums[0], nums[1])
        # n = 3, dp[2] = max(dp[1], dp[0] + num[2])
        n = len(nums)

        dp0 = 0
        dp1 = 0

        for i in range(0, n):
            dp2 = max(dp1, dp0 + nums[i])
            dp1, dp0 = dp2, dp1

        return dp2
        