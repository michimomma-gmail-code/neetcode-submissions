class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # temp = n & 1
        # res << 1 
        # res |= temp
        # n >> 1

        for _ in range(32):
#            temp = n & 1
            res = (res << 1) | (n & 1)
            n >>= 1

        return res
