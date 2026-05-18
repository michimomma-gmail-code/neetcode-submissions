class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n = len(t)
        chars = list(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        # s = "caat": [c, a, a, t]
        # t = "cat" (n = 3)
        # char = "c"
        # i = 3, t[n - 1 (2)]: t
        # i = 2, t[n - 2 (1)]: a
        # i = 1, t[n - 3 (0)]: c -> dp[1] : dp[1] = dp[0] (True)
        # char = a ([c, <a>, a, t])
        # i = 3, t[n - 1 (2)]: t
        # i = 2, t[n - 2 (1)]: a -> dp[2]: dp[2] = dp[1]
        # char = a ([c, a, <a>, t])
        # i = 3, t[n - 1 (2)]: t
        # i = 2, t[n - 2 (1)]: a -> dp[2]: dp[2] = dp[1]
        # char = t ([c, a, a, <t>)
        # i = 3, t[n - 1 (2)]: t -> dp[3]: dp[3] = dp[2]
        #

        for j in range(len(chars)):
            char = chars[j]
            for i in range(n, 0, -1):
                if char == t[i - 1]:
                    dp[i] += dp[i - 1]

        print(dp)

        return dp[n]