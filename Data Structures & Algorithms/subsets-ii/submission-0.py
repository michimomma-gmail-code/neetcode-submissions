class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = nums.copy()

        nums.sort()

        result = []
        subset = []

        def dfs(start):
            result.append(subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
    
        dfs(0)
        return result
    