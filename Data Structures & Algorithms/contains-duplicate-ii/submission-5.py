class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        # [1, 2, 3, 1], k = 3
        # [(1), 2, 3, (1)], k = 3
        # right = k, left = 0
        # 
        # [2, 1, 2], k = 1
        # right = 1, left = 0
        # right = 2, left = 1
        # 
        # 1. store (k) elem in hashtab (counts)
        # 2. examine nums[right] has dup
        # 3. if false, add nums to the hashtab, and reduce counts (if 0 remove) nums[left] to keep k-items 
        #
        mem = {}
        for right in range(len(nums)):
            print(len(mem))
            print(nums[right])

            # if right < k:
            #     mem[nums[right]] = 1 + mem.get(nums[right], 0)
            #     continue

            if nums[right] in mem:
                return True
            
            mem[nums[right]] = 1 + mem.get(nums[right], 0)

            if right >= k:
                left = right - k
                if mem[nums[left]] <= 1:
                    del mem[nums[left]]
                else:
                    mem[nums[left]] -= 1
            
        return False
            

            
