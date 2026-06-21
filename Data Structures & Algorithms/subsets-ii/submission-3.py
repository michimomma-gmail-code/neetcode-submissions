class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)

        results = []
        subset = []

        def dfs(index):
            results.append(subset.copy())

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        dfs(0)

        return results

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [1a 1b 2]
        # [1a 1b] [1a 2]
        # [1b 2]
        
        nums = sorted(nums)
        n = len(nums)

        results = []
        subset = []

        def dfs(index):
            if index >= n:
                results.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()

            # find nums[index] != nums[index + k]
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1)

        dfs(0)

        return results
