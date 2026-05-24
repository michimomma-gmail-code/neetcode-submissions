class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # 0. res = x
        # 1. res = res * res = x = x ** 2
        # 2. res = res * res = x ** 4
        # 3. res = res * res = x ** 16
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        def dfs(x, n):
            if n == 1:
                return x
            
            res = dfs(x, n // 2)
            if n % 2 == 0:
                return res * res
            else:
                return res * res * x

        res = dfs(x, abs(n))
        return res if n > 0 else 1 / res

        
