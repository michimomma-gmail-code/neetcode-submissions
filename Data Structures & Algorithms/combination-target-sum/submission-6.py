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



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = nums.copy()
        nums.sort()

        print(nums)

        res = []
        subset = []        
        def dfs(i, cur_total):
            if cur_total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or cur_total > target:
                return

            for j in range(i, len(nums)):
                cur_total += nums[j]
                if cur_total > target:
                    return
                subset.append(nums[j])
                dfs(j, cur_total)
                subset.pop()
                cur_total -= nums[j]

        dfs(0, 0)

        return res






































