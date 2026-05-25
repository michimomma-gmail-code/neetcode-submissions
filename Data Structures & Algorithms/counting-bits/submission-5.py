class Solution:
    def countBits0(self, n: int) -> List[int]:
        
        def compute(n):
            res = 0
            while n > 0:
#                n = n & (n - 1)
                res += n & 1
                n = n >> 1
#                n >>= 1
                #res += 1
            return res

        res = []
        for i in range(n + 1):
            res.append( compute(i) )

        return res

    def countBits(self, n: int) -> List[int]:
        # n = 1, 01 & 1
        # n = 2, 010 & 1, 001 & 1
        # n = 3, 011 & 1, 001 & 1
        # n = 4, 100 & 1, 010 & 1, 001 & 1
        # n = 5, 101 & 1, 010 & 1, 001 & 1

        # dp[0] = 0
        # dp[1] = 1
        # dp[n] = dp[n >> 1] + n & 1

        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
#            dp[i] = dp[i & (i - 1)] + 1
        return dp

