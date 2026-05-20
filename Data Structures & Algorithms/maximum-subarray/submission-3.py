class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
#        dp = [*nums]

#        print(dp)

        dp = nums[0]
        maxdp = dp
        for i in range(1,  n ):
            num = nums[i]
            dp = max(dp + num, num)
            maxdp = max(maxdp, dp)

        return maxdp