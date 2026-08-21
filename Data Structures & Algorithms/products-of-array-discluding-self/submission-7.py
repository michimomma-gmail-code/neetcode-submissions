class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]

        #  [1,  2,  8, 48]: a_l
        # [48, 48, 24,  6]: a_r

        a_l, a_r = nums.copy(), nums.copy()
        cum = 1
        for i in range(len(nums)):
            num = nums[i]
            a_l[i] = cum * num
            cum *= num

        cum = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            a_r[i] = cum * num
            cum *= num

        res = []
        for i in range(len(nums)):
            r = 1
            if (i + 1) < len(nums):
                r = a_r[i + 1]
            l = 1
            if (i - 1) >= 0:
                l = a_l[i - 1]
            res.append(r * l)
        
        return res
