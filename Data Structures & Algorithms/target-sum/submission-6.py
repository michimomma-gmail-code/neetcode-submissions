class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # target - num: 
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = total
        total = sum(nums)

        if abs(target) > total or (target + total) % 2 != 0:
            print(f'target = {target}, total = {total}')
            return 0

        amount = (target + total) // 2
        #
        dp = [0] * (amount + 1)
        dp[0] = 1

        for num in nums:
            for a in range(amount, num -1, -1):
#                print(f'a = {a}, num = {num}')
                if a >= num and dp[a - num] > 0:
                    dp[a] += dp[a - num]

        return dp[amount]            
        

