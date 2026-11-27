class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]

        #          [1,  2,  8, 48]: a_l
        # [48, 48, 24,  6]: a_r

        #
        nz = 0
        idx_z = None
        temp = 1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                nz += 1
                idx_z = i
            else:
                temp *= num

        res = [0] * len(nums)
        if nz > 1:
            return res
        elif nz == 1:
            res[idx_z] = temp
            return res
        #
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



    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 2, 8, 48]
        # [48, 48, 24, 6]

        p1 = []
        cum = 1
        for num in nums:
            cum *= num
            p1.append(cum)

#        print(p1)
        p2 = []
        cum = 1
        for i in range(len(nums) - 1, -1, -1):
            cum *= nums[i]
            p2.append(cum)
#        print(p2)

        res = []
        for i in range(len(nums)):
            pre = 1
            if i - 1 >= 0:
                pre = p1[i - 1]
            
            post = 1
            if i + 1 <= len(p2) - 1:
                post = p2[len(p2) -1 - (i + 1)]

            res.append(pre * post)

        return res






















