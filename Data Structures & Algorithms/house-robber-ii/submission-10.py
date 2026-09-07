class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # s1: can take 1st, not take last
        rob = - 1
        nothing = 0
        for i in range(0, len(nums) - 1):
            rob, nothing = nothing + nums[i], max(nothing, rob)

        print(rob, nothing)
        s1 = max(rob, nothing)
        # s2: cannot take 1st, can take last
        rob = - 1
        nothing = 0
        for i in range(1, len(nums)):
            rob, nothing = nothing + nums[i], max(nothing, rob)

        print(rob, nothing)
        s2 = max(rob, nothing)

        return max(s1, s2)
