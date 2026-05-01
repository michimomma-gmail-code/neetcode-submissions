class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        selected = [False for num in nums]

        def dfs(selected):

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i, num in enumerate(nums):

                if not selected[i]:
                    subset.append(num)
                    selected[i] = True
                    dfs(selected)
                    subset.pop()
                    selected[i] = False
        
        dfs(selected)

        return result