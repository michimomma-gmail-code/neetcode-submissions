class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        temp = []
        nums = list(nums)

        selected = [False for _ in range(len(nums))]

        def dfs():
            if len(temp) == len(nums):
                results.append(temp.copy())

            for i in range(len(nums)):
                if not selected[i]:
                    selected[i] = True
                    temp.append(nums[i])
                    dfs()
                    temp.pop()
                    selected[i] = False

        dfs()
        
        return results