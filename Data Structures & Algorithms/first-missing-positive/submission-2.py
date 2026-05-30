class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [-2, -1, 0] -> [-2, -1, 0] vs [1, 2, 3] -> 1 is missing
        # [1, 2, 4] -> [1, 2, 3] -> 3 is missing
        # [1, 2, 4, 5, 6, 3, 1] -> [1, 2, 3, 4, 5, 6, 1] -> 7 is missing
        # [4, 2, 1] -> [1, 2, 4]
        n = len(nums)
        # [1, 2, ..., n]
        for i in range(n):

            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                new_idx = nums[i] - 1
                old_idx = i
                nums[new_idx], nums[old_idx] = nums[old_idx], nums[new_idx]
        
#        print(nums)

        for i in range(n):
            expected = i + 1
            if nums[i] != expected:
                return expected
        return n + 1

