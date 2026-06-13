class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        res = []
        current_xor2 = 0
        def dfs(start, current_xor):
            nonlocal current_xor2
            if start == n:
                res.append(current_xor2)
                return current_xor

            current_xor2 ^= nums[start]
            pick = dfs(start + 1, current_xor ^ nums[start])

            current_xor2 ^= nums[start]
            skip = dfs(start + 1, current_xor)

            return pick + skip

        temp = dfs(0, 0)
#        print(res)
        return sum(res)
