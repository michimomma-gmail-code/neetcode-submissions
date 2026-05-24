class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        res = []
        for i in range(n - 1, -1, -1):
            num = digits[i] + carry
            if num >= 10:
                carry = num // 10
                num = num % 10
            else:
                carry = 0
            res.append(num)
        if carry > 0:
            res.append(carry)
        
        res.reverse()
        return res