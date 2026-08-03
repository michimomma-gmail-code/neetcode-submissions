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
