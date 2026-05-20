class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("infinity")] + [*nums]

        print(dp)

        for i in range(1,  n + 1 ):
            num = nums[i - 1]
            dp[i] = max(dp[i - 1] + num, num)

        return max(dp)