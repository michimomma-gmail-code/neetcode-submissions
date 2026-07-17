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



    def convertToTitle0(self, columnNumber: int) -> str:
        # cn 
        # 1 2   3  4    5   6    7   8  9   10 11 12
        # A B  AA AB   BA  BB  AAA AAB ABA ABB A B

        # 27^2 27^1 27^0
        #
        temp = []
        def dfs(cn):
            nonlocal temp
            if cn == 0:
                return 0

            num = cn - 1
#            print('num = ', num)
#            print(chr(num % 26 + ord("A")))
            temp.append(chr(num % 26 + ord("A")))
            res = dfs( num // 26)
#            print('res = ', res)           
            return res

        res = dfs(columnNumber)
#        print(temp)
        temp.reverse()
        return "".join(temp)

