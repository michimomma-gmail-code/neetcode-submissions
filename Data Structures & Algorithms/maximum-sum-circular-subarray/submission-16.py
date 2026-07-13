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



    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = cur_max = nums[0]
        min_sum = cur_min = nums[0]

        total = sum(nums)

        for i in range(1, n):
            num = nums[i]
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)


