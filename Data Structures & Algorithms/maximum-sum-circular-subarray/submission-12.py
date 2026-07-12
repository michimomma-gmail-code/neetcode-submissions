class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
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


    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        cur_p, cur_n = 0, 0
        total = sum(nums)
        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(len(nums)):
            if cur_p < 0:
                cur_p = 0
            if cur_n > 0:
                cur_n = 0
            cur_p += nums[i]
            cur_n += nums[i]
            max_sum = max(max_sum, cur_p)
            min_sum = min(min_sum, cur_n)
        print(max_sum, min_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum, max(nums))
