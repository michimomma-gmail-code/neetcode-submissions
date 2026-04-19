class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_unique = len(set(nums))
        return num_unique < len(nums)
