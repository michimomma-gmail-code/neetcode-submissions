class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]

        if temp % 2 > 0:
            return False

        target = temp // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, 0, -1):
                if i - num < 0:
                    continue
                if dp[i - num]:
                    dp[i] = True

        return dp[target ]