class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [ False for _ in range(n + 1) ]
        # dp[n] = dp[n - len(word)] (adding len(word) will reach n)
        dp[0] = True            

        for i in range(1, n + 1):

            if not dp[i - 1]:
                continue

            for word in wordDict:
#                print(f'{s}, {s[i - 1 : i - 1 + len(word)]}, {word}')
                if s[i - 1 : i - 1 + len(word)] == word and dp[i - 1]:
                    dp[i - 1 + len(word)] = True

#        print(dp)

        return dp[n]

        