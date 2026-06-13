class Solution:
    def combine0(self, n: int, k: int) -> List[List[int]]:
        
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

    def combine1(self, n: int, k: int) -> List[List[int]]:
            res = []
            subset = []
            
            # 'i' is the specific number we are currently looking at
            def dfs(i):
                # 1. Success Base Case: Our basket is full!
                if len(subset) == k:
                    res.append(subset.copy())
                    return
                    
                # 2. Failure Base Case (The Sniper Optimization):
                # If the numbers we have left + the numbers currently in our basket 
                # are less than k, it is mathematically impossible to finish. Stop searching.
                if len(subset) + (n - i + 1) < k:
                    return
                    
                # Branch A: PICK the current number
                subset.append(i)
                dfs(i + 1)
                subset.pop()  # Undo the pick to prepare for the alternate universe
                
                # Branch B: SKIP the current number
                dfs(i + 1)
                
            dfs(1)
            return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        subset = []
    
        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i > n:
                return
                
            subset.append(i)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(1)

        return res