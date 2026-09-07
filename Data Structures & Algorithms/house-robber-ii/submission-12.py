class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def runDP(st, ed):
            rob = - 1
            nothing = 0
            for i in range(st, ed):
                rob, nothing = nothing + nums[i], max(nothing, rob)

#            print(rob, nothing)
            return max(rob, nothing)

        # s1: can take 1st, not take last
        s1 = runDP(0, len(nums) - 1)
        # s2: cannot take 1st, can take last
        s2 = runDP(1, len(nums))

        return max(s1, s2)
