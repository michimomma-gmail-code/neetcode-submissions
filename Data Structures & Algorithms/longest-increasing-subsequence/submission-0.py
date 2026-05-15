class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]: longest increasing subsequence ending at i (num[i])
        # dp[0]: 0
        # dp[1]: 1
        # given, dp[j, j < i], dp[i]: dp[j] + 1 if nums[i] > nums[j]

        dp = [1 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            for j in range(0, i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)