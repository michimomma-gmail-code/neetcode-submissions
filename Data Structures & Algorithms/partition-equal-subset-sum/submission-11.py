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


    def canPartition(self, nums: List[int]) -> bool:
        # total = subset1 + subset2 = 2 * subset
        # subset = total / 2
        #
        total = sum(nums)
        print(total)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for j in range(len(nums)):
            k = nums[j]
            for i in range(len(dp)-1, 0, -1):
                if dp[i - k] and i >= k:
                    dp[i] = True

        print(dp)
        return dp[-1]
















