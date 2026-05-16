class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n + 1)

        # dp[i - len(word)] is True -> dp[i] is True

        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:

                if word == s[i - len(word): i] and i - len(word) >= 0 and dp[i - len(word)]:
                    dp[i] = True

        return dp[n]