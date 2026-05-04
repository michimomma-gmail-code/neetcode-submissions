class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = list(candidates)
        candidates.sort()

        results = []
        subset = []

        def dfs(i, cur):

            if cur == target:
                results.append(subset.copy())
                return

            if cur > target:
                return

            for j in range(i, len(candidates)):
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                subset.append(candidates[j])
                dfs(j + 1, cur + candidates[j])
                subset.pop()

        dfs(0, 0)

        return results
