class Solution:
    def maxCoins0(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def dfs(left, right):

            if left + 1 == right:
                return 0
            
            if (left, right) in memo:
                return memo[ (left, right) ]

            max_res = 0
            for i in range(left + 1, right):

                left_res = dfs(left, i)
                right_res = dfs(i, right)

                val = left_res + nums[left] * nums[i] * nums[right] + right_res
                max_res = max(max_res, val)
            
            memo[ (left, right) ] = max_res

            return max_res

        return dfs(0, n - 1)

    def maxCoins(self, nums: List[int]) -> int:
# Pad the boundaries
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[l][r] = max coins strictly between index l and r
        dp = [[0] * n for _ in range(n)]
        
        # Outer Loop: The 'window size' or 'length' of the interval between l and r.
        # It starts at 2 because we need at least 1 balloon strictly between l and r.
        for length in range(2, n):
            
            # Slide the left boundary across the array
            for left in range(0, n - length):
                
                # The right boundary is fixed by the left boundary and the current length
                right = left + length
                
                # Test every balloon 'i' as the LAST one to burst in this interval
                for i in range(left + 1, right):
                    
                    coins = (dp[left][i] + 
                             (nums[left] * nums[i] * nums[right]) + 
                             dp[i][right])
                             
                    dp[left][right] = max(dp[left][right], coins)
                    
        # Return the max coins for the entire interval (0 to n-1)
        return dp[0][n - 1]
