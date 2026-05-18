class Solution:
    def isInterleave0(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        dp = [ [False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        dp[0][0] = True

        for r in range(0, len(s1) + 1):
            for c in range(0, len(s2) + 1):
                if r == 0 and c == 0:
                    continue
                if (r > 0) and dp[r - 1][c] and s1[r - 1] == s3[r + c - 1]:
                    dp[r][c] = True
                elif (c > 0) and dp[r][c - 1] and s2[c - 1] == s3[r + c - 1]:
                    dp[r][c] = True

        return dp[len(s1)][len(s2)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        if len(s3) != len(s1) + len(s2):
            return False

#        dp = [ [False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp = [False] * (len(s2) + 1)

        dp[0] = True
#        prev_dp = dp.copy()

        for r in range(0, len(s1) + 1):
            for c in range(0, len(s2) + 1):
                if r == 0 and c == 0:
                    continue
                if ((r > 0) and dp[c] and s1[r - 1] == s3[r + c - 1]) or ((c > 0) and dp[c - 1] and s2[c - 1] == s3[r + c - 1]):
                    dp[c] = True
                else:
                    dp[c] = False
#            prev_dp = dp.copy()

        return dp[len(s2)]

