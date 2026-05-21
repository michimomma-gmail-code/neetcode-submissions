class Solution:
    def canJumpD(self, nums: List[int]) -> bool:
        # dp[i] = True if dp[i-1] + nums[i] >= n
        # dp[0] = False
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i and dp[j]:
                    dp[i] = True

        return dp[n - 1]

    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0
        n = len(nums)

        for i in range(len(nums)):

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n - 1: 
                return True
        
        return False

