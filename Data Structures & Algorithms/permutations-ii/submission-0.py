class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        
        results = []
        temp = []    
        n = len(nums)

        selected = set()

        # [1a,1b,2]
        # [1b,1a,2]
        # -- when encounter 1a in the 2nd time, don't proceed 
        # selected - prevents same index to be taken
        # 

        def dfs():
            if len(temp) == n:
                results.append(temp.copy())
                return

            for i in range(n):
                    
                num = nums[i]
                if i not in selected:
                    if i > 0 and nums[i - 1] == nums[i] and (i - 1) not in selected:
                        continue
                    selected.add(i)
                    temp.append(num)
                    dfs()
                    selected.remove(i)
                    temp.pop()

        dfs()

        return results
