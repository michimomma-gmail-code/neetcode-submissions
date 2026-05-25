class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = [num + 1 for num in nums]
        # 1 2
        # (1 + 2) * 2 / 2 = 3
        # 1 2 3
        # (1 + 3) * 3 / 2 = 6
        # [1, 2, 3] -> [2, 3, 4]
        #
        total = sum(nums)
        
        # [2, 3, 4] -> [1, 2, 3, 4]
        expected = (1 + (n)) * (n) // 2 
        # (1 + 4) * 4 / 2 = 10

#        print(f'expected = {expected} total = {total}')

        return expected - total 
    
    def missingNumber(self, nums: List[int]) -> int:
        
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res