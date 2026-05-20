class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        jumps = 1
        farthest = nums[0]
        current_window_end = nums[0]

        for i in range(1, len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_window_end:
                jumps += 1
                current_window_end = farthest
        
                if current_window_end >= len(nums) - 1:
                    break

        return jumps

    def jumpD(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):

                if j + nums[j]  >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
        print(dp)
        return dp[n - 1]        

        
