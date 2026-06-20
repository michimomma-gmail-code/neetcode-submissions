class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)

        results = []
        subset = []

        def dfs(index):
            results.append(subset.copy())

            prev = None
            for i in range(index, n):
                if nums[i] == prev:
                    continue
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
                prev = nums[i]
        dfs(0)

        return results
