class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for k in count:
            if count[k] > 1:
                return True
        return False