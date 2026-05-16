class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + 1)
                else:
                    dp[r][c] = max(dp[r -1][c], dp[r][c - 1])

        return dp[m][n]
                    