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

    def checkValidString(self, s: str) -> bool:

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
