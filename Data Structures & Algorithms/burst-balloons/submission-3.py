class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]

        memo = {}

        def dfs(left, right):
            if left + 1 == right:
                return 0

            if (left, right) in memo:
                return memo[ (left, right) ]

            max_res = 0
            for i in range(left + 1, right):
                left_res = dfs(left, i)
                right_res = dfs(i, right)

                total = left_res + nums[left] * nums[i] * nums[right] + right_res

                max_res = max(max_res, total)

            memo[ (left, right) ] = max_res
        
            return max_res

        return dfs(0, len(nums) - 1)