class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev1 = prev2 = 0
        n = len(cost)

        for i in range(2, n + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev1, prev2 = curr, prev1

        return curr