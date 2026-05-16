class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = res = nums[0]

        for i in range(1, len(nums)):
            temp = max(cur_max * nums[i], cur_min * nums[i], nums[i])
            cur_min = min(cur_max * nums[i], cur_min * nums[i], nums[i])
            cur_max = temp

            res = max(res, cur_max)
        return res