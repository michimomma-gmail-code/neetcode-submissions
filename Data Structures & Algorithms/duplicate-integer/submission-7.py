class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#        prev = nums[0]
        if not nums:
            return False
        seen = {nums[0]}
        for i in range(1, len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False