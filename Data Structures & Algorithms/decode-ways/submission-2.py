class Solution:
    def numDecodings0(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [ 0 for _ in range(n + 1)]

        dp[0] = 1
        dp[1] = 1

        # i = 2, s = 10, 11, ..., 99
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        n = len(s)
        if n == 1:
            return 1
#        dp = [ 0 for _ in range(n + 1)]

        dp0 = 1
        dp1 = 1

        # i = 2, s = 10, 11, ..., 99
        for i in range(2, n + 1):
            dp2 = 0
            if s[i - 1] != '0':
#                dp[i] += dp[i - 1]
                dp2 += dp1
#                dp1 = dp2

            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
#                dp[i] += dp[i - 2]
                dp2 += dp0
#                dp0 = dp1
        
            dp0, dp1 = dp1, dp2

        return dp2
