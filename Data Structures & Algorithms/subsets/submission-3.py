class Solution:
    def subsets0(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            new_subset = [current_subset + [num] for current_subset in results]
            results.extend(new_subset)
        
        return results

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
#            if i >= len(nums):
            result.append(subset.copy())
#                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()

        dfs(0)
        return result