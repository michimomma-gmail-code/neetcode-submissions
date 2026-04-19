class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_unique = len(set(nums))
        if num_unique < len(nums):
            return True
        else:
            return False