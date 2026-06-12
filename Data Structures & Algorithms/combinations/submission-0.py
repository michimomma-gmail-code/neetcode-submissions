class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        subset = []
    
        def dfs(i):
            if len(subset) >= k:
                return res.append(subset.copy())
                
            for j in range(i, n + 1):
                subset.append(j)
                dfs(j + 1)
                subset.pop()

        dfs(1)

        return res