class Solution:
    def checkValidStringT(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False


        while open_stack and star_stack:

            if not (open_stack[-1] < star_stack[-1]):
                return False

            open_stack.pop()
            star_stack.pop()

        return not open_stack

    def checkValidStringd(self, s: str) -> bool:

        memo = {}

        def dfs(i, open_count):
            if open_count < 0:
                return False
            if i == len(s):
                return open_count == 0
            
            if (i, open_count) in memo:
                return memo[ (i, open_count) ]

            char = s[i]

            if char == "(":
                res = dfs(i + 1, open_count + 1)
            elif char == ")":
                res = dfs(i + 1, open_count - 1)
            else:
                opt1 = dfs(i + 1, open_count + 1)
                opt2 = dfs(i + 1, open_count - 1)
                opt3 = dfs(i + 1, open_count)

                res = opt1 or opt2 or opt3
            
            memo[ (i, open_count) ] = res

            return res

        return dfs(0, 0)

    def checkValidString(self, s: str) -> bool:
        n = len(s)

        # dp[i][j] = True if s[i:] is valid given j currently open parenthesis
        dp = [ [False] * (n + 1) for _ in range(n + 1) ]

        dp[n][0] = True

        for i in range(n - 1, -1, -1):

            for j in range(n):

                if s[i] == "(":
                    dp[i][j] = dp[i + 1][j + 1]
                elif s[i] == ")":
                    if j >= 1:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    res = dp[i + 1][j] or dp[i + 1][j + 1]
                    if j >= 1:
                        res = res or dp[i + 1][j - 1]
                    dp[i][j] = res
                    
        return dp[0][0]

