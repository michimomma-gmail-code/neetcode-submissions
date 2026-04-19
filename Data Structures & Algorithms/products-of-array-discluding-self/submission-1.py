class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # before
    # Input:
    # nums=[1,2,4,6]
    # stdout:
    # [1, 2, 8, 48]
    # [6, 24, 48, 48]        

        fac = 1
        pre_res = []
        for i in range(len(nums)):
            fac *= int(nums[i])
            pre_res.append(fac)
        
        post_res = []
        fac = 1
        for i in range(len(nums)-1, -1, -1):
            fac *= int(nums[i])
            post_res.append(fac)
        post_res.reverse()

        print(pre_res)
        print(post_res)

        res = []
        for i in range(len(pre_res)):
            if i == 0:
                res.append(post_res[i+1])
            elif i == len(pre_res)-1:
                res.append(pre_res[i-1])
            else:
                res.append(pre_res[i-1] * post_res[i+1])

        return res

