class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)

        res = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            print(nums[i])
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])

        print(dp)
        return res

    def maxSubArray1(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num

            max_sum = max(max_sum, current_sum)

        return max_sum
        

#    def maxSubArray(self, nums: List[int]) -> int:
        # state: active, start
        # active[i] = max(active[i -1] + nums[i], start[i])
        # start[i] = nums[i]

