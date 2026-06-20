class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        temp = []
        selected = [False] * n

        def dfs():
            
            if len(temp) == n:
#                print(f'result: {temp}')
                results.append(temp.copy())

            for i in range(n):
                num = nums[i]
                if not selected[i]:
                    temp.append(num)
                    selected[i] = True
                    dfs()
                    temp.pop()
                    selected[i] = False

        dfs()

        return results

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        temp = []
        visited = set()

        def dfs():
            
            if len(temp) == n:
                results.append(temp.copy())
                return

            for num in nums:
                if num in visited:
                    continue

                temp.append(num)
                visited.add(num)
                dfs()
                temp.pop()
                visited.remove(num) 
                               
        dfs()

        return results
