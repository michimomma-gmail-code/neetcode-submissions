class Solution:
    def reverse(self, x: int) -> int:
        MAXINT = (1 << 31) - 1
#        2147483647
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            pop = x % 10
            x = x // 10
            # check res * 10 + pop is within limit
            if res > MAXINT // 10:
                return 0
            if res > MAXINT // 10 and pop > 7:
                return 0
            res = res * 10 + pop 

        return sign * res
