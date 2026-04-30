class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            new_subset = [current_subset + [num] for current_subset in results]
            results.extend(new_subset)
        
        return results