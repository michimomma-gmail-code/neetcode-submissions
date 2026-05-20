class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)

        res = nums[0]
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
            res = max(res, dp[i])

        return res