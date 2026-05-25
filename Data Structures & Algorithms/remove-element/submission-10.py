class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        # if len(nums) == 1:
        #     if nums[0] == val:
        #         nums.pop()
        #         return 0
        #     else:
        #         return 0

        l, r = 0, len(nums) - 1
        # nums[l] == val, nums[r] != val, switch
        # if nums[l] == val, nums[r] == val
        #.   l unchange, r -= 1,  
        # if nums[l] != val, nums[r] == val, 
        #.   l += 1, r -= 1
        # if nums[l] != val, nums[r] != val
        #.   l +- 1, r unchange

        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] != val:
                l += 1
            if nums[r] == val:
                r -= 1
        
#        print(nums)
#        print(f'l = {l}, r = {r}')
        return l