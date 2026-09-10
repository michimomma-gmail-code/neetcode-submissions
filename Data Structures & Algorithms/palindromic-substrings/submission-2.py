class Solution:
    def countSubstringsD(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [ [False for _ in range(n)] for i in range(n) ]
        # len = 1
        for i in range(n):
            dp[i][i] = True
            count += 1

        # len = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # len >= 3
        for l in range(3, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    break
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    count += 1

        return count

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.count = 0

        def search(l, r):
            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                self.count += 1

        for i in range(n):
            search(i, i)
            search(i, i + 1)

        return self.count                


