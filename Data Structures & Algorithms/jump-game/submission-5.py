class Solution:
    def canJump0(self, nums: List[int]) -> bool:
        # nums   =    [1, 1] (n = 2)
        # index  = [0, 1] (dp)
        # i = 1, assume dp[1] is T, i + nums[i - 1] = 1 + nums[0] = 2, dp[i + 1 = 2] = T

        # target = 2
        # i = 2, assume dp[i - 1 = 1] is T, (i - 1) + nums[i - 2] = 1 + nums[0] = 2, dp[i = 2] = T
        #
        # target = 3
        # i = 3, assume dp[i - 1 = 2] is T, (i - 1) + nums[i - 2] = 2 + nums[1] = 3, dp[i = 3] = T
        # target = 4
        # i = 4, assume dp[i - 1 = 3] is T, (i - 1) + nums[i - 2] = 3 + nums[2] = 3, dp[i = 4] = F


        # nums =      [1, 1, 0] (n = 3)
        # index  = [0, 1, 2]
        # i = 2, assume dp[2] is T, i + nums[i - 1] = 2 + nums[1] = 2 + 1 = 3, dp[i + 1 = 3] = T

        # nums =      [1, 1, 0, 1] (n = 4)
        # index  = [0, 1, 2]
        # i = 3, assume dp[3] is T, i + nums[i - 1] = 3 + nums[2] = 3 + 0 = 3, dp[i + 1 = 4] = F

        n = len(nums)
        dp = [False] * (n + 1)
        dp[1] = True

        for i in range(2, n + 1):
#        for i in range(n, 1, -1):
            for j in range(2, i + 1):
                if dp[j - 1] and (j - 1) + nums[j - 2] >= i:
                    dp[i] = True
                    break

        return dp[n]

    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [False] * n 
        dp[0] = True

        for i in range(1, n):
            for j in range(0, i):
                if dp[j] and (j + 1) + nums[j] >= i + 1:
                    dp[i] = True
                    break
        return dp[n - 1]


