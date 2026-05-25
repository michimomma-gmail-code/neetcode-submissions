class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def compute(n):
            res = 0
            while n > 0:
#                n = n & (n - 1)
                res += n & 1
                n = n >> 1
#                n >>= 1
                #res += 1
            return res

        res = []
        for i in range(n + 1):
            res.append( compute(i) )

        return res