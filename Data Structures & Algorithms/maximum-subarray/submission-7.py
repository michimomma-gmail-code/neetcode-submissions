class Solution:
    def maxSubArrayDP(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)

        res = nums[0]
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
            res = max(res, dp[i])

        return res

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num

            max_sum = max(max_sum, current_sum)

        return max_sum
        