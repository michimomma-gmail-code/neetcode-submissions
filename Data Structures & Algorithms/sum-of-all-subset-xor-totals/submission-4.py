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


    def subsetXORSum1(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = []
        current_xor2 = 0
        def dfs(start):
            nonlocal current_xor2

            if start == n:
                res.append(current_xor2)
                return

            current_xor2 ^= nums[start]
            dfs(start + 1)

            current_xor2 ^= nums[start]
            dfs(start + 1)
            return

        dfs(0)
        return sum(res)
