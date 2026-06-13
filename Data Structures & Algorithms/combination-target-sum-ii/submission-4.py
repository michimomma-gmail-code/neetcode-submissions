class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        freq = {}
        for c in candidates:
            freq[c] = 1 + freq.get(c, 0)

        candidates = [c for c in freq]

#        print(candidates)

        results = []
        subset = []

        def dfs(i, total):

            if total == target:
                results.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            if freq[candidates[i]] == 1:
                dfs(i + 1, total + candidates[i])
            else:
                freq[candidates[i]] -= 1
                dfs(i, total + candidates[i])
                freq[candidates[i]] += 1

            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return results

