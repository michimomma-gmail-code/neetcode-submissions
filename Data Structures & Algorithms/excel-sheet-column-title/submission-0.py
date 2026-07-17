class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # cn 
        # 1 2   3  4    5   6    7   8  9   10 11 12
        # A B  AA AB   BA  BB  AAA AAB ABA ABB A B

        # 27^2 27^1 27^0
        #


        def dfs(cn):
            if cn == 0:
                return ""

            num = cn - 1

            res = dfs( num // 26) + chr(num % 26 + ord("A"))

            return res

        return dfs(columnNumber)