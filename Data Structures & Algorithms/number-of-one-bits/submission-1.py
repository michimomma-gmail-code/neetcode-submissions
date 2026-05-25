class Solution:
    def hammingWeight0(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n & (n - 1)
            res += 1
        return res
