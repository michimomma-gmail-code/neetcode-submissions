class Solution:
    def climbStairs(self, n: int) -> int:
        #dp = [0] * (n + 1)
        if n <= 2:
            return n
            
        prev = 1
        curr = 2

        for _ in range(3, n + 1):
            curr, prev = prev + curr, curr

        return curr