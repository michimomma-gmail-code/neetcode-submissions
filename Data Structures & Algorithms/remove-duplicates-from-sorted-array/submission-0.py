class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ptr = 0
        unique = 0

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            nums[write_ptr] = nums[i]
            write_ptr += 1
            unique += 1

        return unique

        
