class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            tmp = [current_result + [num] for current_result in result]
#            print(tmp)
            result.extend(tmp)

        return result

    def subsets0(self, nums: List[int]) -> List[List[int]]:

        results = []
        subset = []
        def dfs(index):
            if index >= len(nums):
                results.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)

        return results

    def subsetss(self, nums: List[int]) -> List[List[int]]:

        results = []
        subset = []
        n = len(nums)
        def dfs(index):
            results.append(subset.copy())

            for i in range(index, n):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)

        return results

    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        n = len(nums)
        def dfs(index, subset):
            results.append(subset.copy())
            for i in range(index, n):           
                subset.append(nums[i])     
                dfs(i + 1, subset)
                subset.pop()                

        dfs(0, [])

        return results



