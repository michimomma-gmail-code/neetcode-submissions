class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        def dfs(start, current_xor):
            if start == n:
                return current_xor
            pick = dfs(start + 1, current_xor ^ nums[start])
            skip = dfs(start + 1, current_xor)

            return pick + skip

        return dfs(0, 0)
