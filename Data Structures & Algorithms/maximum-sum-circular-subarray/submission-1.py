class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        width = 2
        n = len(nums)

        res = [0] * n
        max_sum = -float("infinity")

        for w in range(n):
            for i in range(n):
                ed = (i + w) % n
#                if ed <= n - 1:
                res[i] += nums[ed]
#                if ed < i:
#                    res[i] += nums[ed - 1]
                max_sum = max(max_sum, res[i])
#            print(f'w = {w}, res = {res}')
        return max_sum