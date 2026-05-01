class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, total):

            if total  == target:
                result.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            subset.append(nums[i])
            total += nums[i]
            dfs(i, total)

            subset.pop()
            total -= nums[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return result