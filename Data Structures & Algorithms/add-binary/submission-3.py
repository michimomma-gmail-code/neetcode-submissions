class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(b) > len(a):
            a, b = b, a

        
        b = "0" * (len(a) - len(b)) + b

        print(a, b)
        res = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            sub = int(a[i]) + int(b[i]) + carry
            print(i, sub)
            if sub <= 1:
                res.append(str(sub))
                carry = 0
            else:
                if sub == 3:
                    res.append("1")
                    carry = 1
                else: # 2
                    res.append("0")
                    carry = 1
        if carry > 0:
            res.append(str(carry))
        res.reverse()
        return "".join(res)

    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i_a, i_b = len(a) - 1, len(b) - 1

        while i_a >= 0 or i_b >= 0 or carry > 0:
            a_val = int(a[i_a]) if i_a >= 0 else 0
            b_val = int(b[i_b]) if i_b >= 0 else 0
            
            total = a_val + b_val + carry
            res.append(total % 2)
            carry = total // 2

            i_a -= 1
            i_b -= 1

        res.reverse()
        return "".join(map(str, res))

