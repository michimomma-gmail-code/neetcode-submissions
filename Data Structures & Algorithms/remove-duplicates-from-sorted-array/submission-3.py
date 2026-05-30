class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ptr = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            
            nums[write_ptr] = nums[i]
            write_ptr += 1

        return write_ptr

        
