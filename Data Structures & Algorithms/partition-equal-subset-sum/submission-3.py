class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1) 
        dp[0] = True

        print(f'target = {target}, nums = {nums}')
        print(dp)

        for num in nums:
            for i in range(target, 0, -1):
                if i - num >= 0 and dp[i - num]:
                    dp[i] = True

        print(dp)

        return dp[target]


