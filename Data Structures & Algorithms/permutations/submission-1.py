class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs():

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for num in nums:

                if num in subset:
                    continue

                subset.append(num)
                dfs()
                subset.pop()

        
        dfs()

        return result