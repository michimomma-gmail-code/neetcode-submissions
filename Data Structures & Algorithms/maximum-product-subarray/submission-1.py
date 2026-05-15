class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max = nums[0]
        cur_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            _max = max(cur_max * num, num, cur_min * num)
            cur_min = min(cur_min * num, num, cur_max * num)
            cur_max = _max

            global_max = max(global_max, cur_max)

        
        return global_max