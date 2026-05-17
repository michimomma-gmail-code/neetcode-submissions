class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total: 
            return 0
        amount = (total + target) // 2 
        print(f'total = {total}, target = {target}, amount = {amount}')

        dp = [0] * (amount + 1)
        dp[0] = 1

        for num in nums:
            for a in range(amount, num - 1, -1):
                if a >= num:
                    dp[a] += dp[a - num]

        return dp[amount]

