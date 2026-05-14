class Solution:
    def rob0(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        nums.append(0)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
#        dp[2] = dp[1] or dp[0] + nums[2]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n]
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
#        dp = [0] * (n + 1)
#        nums.append(0)

        dp2 = nums[0]
        if n == 1:
            return dp2
        dp1 = max(nums[0], nums[1])
        if n == 2:
            return dp1
        dp0 = 0
#        dp[2] = dp[1] or dp[0] + nums[2]
        for i in range(2, n):
            dp0 = max(dp1, dp2 + nums[i])
            dp1, dp2 = dp0, dp1
        return dp0

    def rob(self, nums: List[int]) -> int:
#        n = len(nums)
        t1 = 0
        t2 = 0
        for num in nums:
            t3 = max(t2, t1 + num)
            t2, t1 = t3, t2
        
        return t3
        