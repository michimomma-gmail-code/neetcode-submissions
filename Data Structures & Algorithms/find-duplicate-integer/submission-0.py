class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1 2 2 3] vs [1 2 3 3] vs [1 2]
        # 
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                return abs(num)
            nums[abs(num)-1] *= -1

        print(nums)

        return -1