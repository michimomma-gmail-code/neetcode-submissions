class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # 345 * 6
        # (300 + 40 + 5) * 6
        # 1. 5 * 6 = 30
        # 2. (4*10) * 6 = 240
        # 3. (3*100) * 6 = 1800
        # 4. sum all 
        # 5. convert each digit in str?

        def num2str(num):
            res = []
            while num > 0:
                dgt = num % 10
                num //= 10
                res.append(str(dgt))
            res.reverse()
            return "".join(res)

        def mult_one_0(n1, n):
            # n1: string
            # n: string
            res = [0] * (len(n1) + len(n))
            for i in range(len(n1) - 1, -1 , -1):
                left = i
                right = i + 1
                v1 = int(n1[i]) * int(n) + res[right]

                res[right] = v1 % 10
                res[left] += v1 // 10

            st = 0
            while st < len(res) and res[st] == 0:
                st += 1

            return "".join(map(str, res[st:]))

        def mult_one(n1, n):
            # n1: string
            # n: string
            if n == "0":
                return "0"
            res = []
            carry = 0
            for i in range(len(n1) - 1, -1, -1):
                temp = int(n1[i]) * int(n) + carry
                res.append(str( temp % 10 ))
                carry = temp // 10
            if carry > 0:
                res.append(str(carry))
            res.reverse()
            return "".join( res )

        def add_strings(num1, num2):
            res = []
            carry = 0

            p1 = len(num1) - 1
            p2 = len(num2) - 1

            while p1 >= 0 or p2 >= 0 or carry:
                v1 = int(num1[p1]) if p1 >= 0 else 0
                v2 = int(num2[p2]) if p2 >= 0 else 0
                temp = v1 + v2 + carry
                res.append(str(temp % 10))
                carry = temp // 10
                p1 -= 1
                p2 -= 1

            res.reverse()
            return "".join(res)


        if len(num1) < len(num2):
            num1, num2 = num1, num2

        res = "0"
        count = 0
        for i in range(len(num2) - 1, -1, -1):
            temp = mult_one(num1, num2[i])
#            print(f"{num1} x {num2[i]} = {temp}")
            temp = temp + "0" * count
#            print(f"{temp} + {res}")
            res = add_strings(temp, res)
#            print(res)
            count += 1

        return res
