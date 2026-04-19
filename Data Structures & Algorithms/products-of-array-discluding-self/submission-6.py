class Solution:
    def productExceptSelf_1st(self, nums: List[int]) -> List[int]:
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

    def productExceptSelf_0(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res

    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        #
        # at i, it is product of pre[i-1] * post[i+1]
        # i = 0, no pre, so it is post [0]
        # i = n-1, no post, so it is pre[n-2]
        #
        # at i, it is product of pre[i] (prod of nums: 0 thru i-1) * post[i] (prod of nums: i+1 thru n-1)
        # boundary: pre[0] = 1, post[n-1] = 1
        # result (usual case): pre[i] * post[i] (i=1 to n-2, but applicable for i=0 and n-1 due to the boundary setting)

        n = len(nums)
        pre = [1] * n
        post = [1] * n
        
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
            #pre[0]: boundary, not included
            #pre[1] = pre[0] * nums[0]
            #pre[n-1] = pre[n-2] * nums[n-2]
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
            #post[n-1]: boundary, not included
            #post[n-2] = post[n-1] * nums[n-1]
            #post[0] = post[1] * nums[1] 
            
        res = []
        for i in range(n):
            res.append(pre[i] * post[i])

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res