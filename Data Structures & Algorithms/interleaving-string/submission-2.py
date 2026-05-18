class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # dp[r][c] = dp[r][c - 1] and s1[r - 1] == s3[r + c - 1] 

        if len(s3) != len(s1) + len(s2):
            return False

        dp = [ [False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        dp[0][0] = True

        # for r in range(1, len(s1) + 1):
        #     dp[r][0] = dp[r - 1][0] and s1[r - 1] == s3[r - 1]

        # for c in range(1, len(s2) + 1):
        #     dp[0][c] = dp[0][0] and s2[c - 1] == s3[c - 1]

        for r in range(0, len(s1) + 1):
            for c in range(0, len(s2) + 1):
                if r == 0 and c == 0:
                    continue
                if dp[r - 1][c] and s1[r - 1] == s3[r + c - 1]:
                    dp[r][c] = True
                elif dp[r][c - 1] and s2[c - 1] == s3[r + c - 1]:
                    dp[r][c] = True

        return dp[len(s1)][len(s2)]

