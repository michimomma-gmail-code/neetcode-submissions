class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [*nums]

        print(dp)

        for i in range(1,  n ):
            num = nums[i]
            dp[i] = max(dp[i - 1] + num, num)

        return max(dp)