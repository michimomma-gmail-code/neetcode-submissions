class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        cum = 0
        st = 0
#        ed = n - 1
        max_sum = -float("infinity")
        for i in range(n):
            cum = 0
            if nums[i] < 0:
                max_sum = max(max_sum, nums[i])
                continue
            st = i
            ed = st + n
            for j in range(st, ed):
                idx = (j % n)
                cum += nums[idx]
                max_sum = max(max_sum, cum)
        return max_sum



