class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        #
        mem = set()
        for right in range(len(nums)):

            # if right < k:
            #     mem[nums[right]] = 1 + mem.get(nums[right], 0)
            #     continue

            if nums[right] in mem:
                return True
            
            mem.add(nums[right])

            if right >= k:
                left = right - k
                mem.remove(nums[left])
            
        return False
            

            
