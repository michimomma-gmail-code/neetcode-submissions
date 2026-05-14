class Solution:
    def rob0(self, nums: List[int]) -> int:
        n = len(nums)
        # A ignore last house (nums[n])
        # B ignore first house (nums[0])
        # A

        if n == 1:
            return nums[0]

        dp0 = dp1 = dp2 = 0
        for i in range(n-1):
            dp2 = max(dp1, dp0 + nums[i])
            dp1, dp0 = dp2, dp1

        dpB0 = dpB1 = dpB2 = 0
        for i in range(1, n):
            dpB2 = max(dpB1, dpB0 + nums[i])
            dpB1, dpB0 = dpB2, dpB1

        res = max(dp2, dpB2)
        return res

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # A ignore last house (nums[n])
        # B ignore first house (nums[0])
        # A

        if n == 1:
            return nums[0]

        def rob_linear(st, ed):
            dp0 = dp1 = dp2 = 0
            for i in range(st, ed):
                dp2 = max(dp1, dp0 + nums[i])
                dp1, dp0 = dp2, dp1
            return dp2

        a = rob_linear(0, n - 1)
        b = rob_linear(1, n)

        return max(a, b)
        