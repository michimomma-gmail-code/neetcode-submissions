class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [ False for _ in range(n + 1) ]
        # dp[n] = dp[n - len(word)] (adding len(word) will reach n)
        dp[0] = True            

        for i in range(n + 1):

            if not dp[i]:
                continue

            for word in wordDict:
#                print(f'{s}, {s[i : i + len(word)]}, {word}')
                if s[i : i  + len(word)] == word and dp[i]:
                    dp[i + len(word)] = True

#        print(dp)

        return dp[n]

        