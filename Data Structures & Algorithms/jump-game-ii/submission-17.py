class Solution:
    def jump(self, nums: List[int]) -> int:

        cur_window = nums[0]
        max_reach = nums[0]
        if len(nums) == 1:
            return 0

        jumps = 1

        for i in range(1, len(nums)):

            if cur_window >= len(nums) - 1:
                return jumps


            if cur_window < i:
                cur_window = max_reach
                jumps += 1


            max_reach = max(max_reach, i + nums[i])
            
        return jumps
