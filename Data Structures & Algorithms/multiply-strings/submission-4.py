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

        def mult_one(n1, n):
            # n1: string
            # n: string
            total = 0
            count = 0
            for i in range(len(n1) - 1, -1 , -1):
                v1 = int(n1[i]) * int(n)
                total += v1 * (10 ** count )
                count += 1
            return total

        if len(num1) < len(num2):
            num1, num2 = num1, num2

        count = 0
        total = 0
        for i in range(len(num2) - 1, -1, -1):
            temp = mult_one(num1, num2[i])
            print(f'{num1} x {num2[i]} = {temp}')
            print(f' res = {temp * (10 ** count)}')
            total += temp * (10 ** count)            
            count += 1

#        print(total)
        res = num2str(total)
        if not res:
            return "0"
#        print(res)
        return res
