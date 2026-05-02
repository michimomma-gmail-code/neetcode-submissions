class Solution:
    def generateParenthesis0(self, n: int) -> List[str]:
        result = []

        def dfs(open_count, close_count, substring):

            if len(substring) == 2 * n:
                result.append(substring)

            if open_count < n:
                dfs(open_count + 1, close_count, substring + "(")
            
            if close_count < open_count:
                dfs(open_count, close_count + 1, substring + ")")

        
        dfs(0, 0, "")
        return result


    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def dfs(open_count, close_count):

            if len(stack) == 2 * n:
                result.append("".join(stack))
            
            if open_count < n:
                stack.append("(")
                dfs(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                dfs(open_count, close_count + 1)
                stack.pop()

        dfs(0, 0)

        return result

        