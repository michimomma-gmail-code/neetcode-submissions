class Solution:
    def combinationSum0(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                results.append(subset.copy())
                return

            
            subset.append(nums[i])
            dfs(i, total + nums[i])

            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return results

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                results.append(subset.copy())
                return

            for i in range(start, len(nums)):

                subset.append(nums[i])
                dfs(i, total + nums[i])
                subset.pop()

        dfs(0, 0)

        return results
