class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [-2, -1, 0] -> [-2, -1, 0] vs [1, 2, 3] -> 1 is missing
        # [1, 2, 4] -> [1, 2, 3] -> 3 is missing
        # [1, 2, 4, 5, 6, 3, 1] -> [1, 2, 3, 4, 5, 6, 1] -> 7 is missing
        n = len(nums)
        # [1, 2, ..., n]
        changed = 1
        while changed > 0:
            changed = 0
            for i in range(n):
                new_idx = nums[i] - 1
                old_idx = i
                if new_idx < 0 or new_idx >= n or nums[new_idx] == nums[old_idx]:
                    continue
                if new_idx != old_idx:
                    nums[new_idx], nums[old_idx] = nums[old_idx], nums[new_idx]
                    changed += 1
        
#        print(nums)

        for i in range(n):
            expected = i + 1
            if nums[i] != expected:
                return expected
        return n + 1

