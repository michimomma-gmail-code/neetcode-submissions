class Solution:
    def rob(self, nums: List[int]) -> int:
        # state
        # rob
        # nothing

        rob = - float("inf")
        nothing = 0

        for num in nums:
            rob, nothing = nothing + num, max(rob, nothing)

#        print(rob, nothing)
        return max(rob, nothing)