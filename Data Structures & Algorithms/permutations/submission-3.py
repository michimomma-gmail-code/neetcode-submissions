class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        selected = {num:False for num in nums}

        def dfs(selected):

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for num in nums:

#                if num in subset:
#                    continue
                if not selected[num]:
                    subset.append(num)
                    selected[num] = True
                    dfs(selected)
                    subset.pop()
                    selected[num] = False

        
        dfs(selected)

        return result