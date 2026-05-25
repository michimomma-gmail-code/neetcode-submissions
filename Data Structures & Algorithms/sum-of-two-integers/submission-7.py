class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 100 + 111 = 1011
        # xor: 011
        # or:  111
        # and: 100 << 1
        # 011 + 1000 = 1011
        # 
        # 01 + 01 = 10
        # xor = 00
        # and = 01 << 10
        # 10 | 00 = 10

#        print(bin(a), bin(b))
        mask = (1 << 32) - 1
#        print(bin(mask))
        res = a & mask
        carry = b & mask
        while carry != 0:

            carry, res = (res & carry) << 1, res ^ carry
            carry &= mask
            res &= mask
#            b = carry
        max_int = (1 << 31) -1
        if res <= max_int:
            return res
        else:
            return ~(res ^ mask)