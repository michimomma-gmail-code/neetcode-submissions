class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        res = []
        def dfs(start, current_xor):
            if start == n:
                res.append(current_xor)
                return current_xor

            pick = dfs(start + 1, current_xor ^ nums[start])
            skip = dfs(start + 1, current_xor)

            return pick + skip

        temp = dfs(0, 0)
#        print(res)
        return sum(res)
