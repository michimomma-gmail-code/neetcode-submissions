class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        nums.append(0)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
#        dp[2] = dp[1] or dp[0] + nums[2]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n]
        