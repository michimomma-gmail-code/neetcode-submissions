class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_5 = 0
        my_bill = {5:0, 10:0, 20:0}

        for i in range(len(bills)):
            reserve = 5 * i

            print(f'bill = {bills[i]}, my_bill =  {my_bill}')
#            ret_amt = bills[i] - 5
            ret_amt = bills[i] - 5
            if ret_amt > reserve:
                return False

            # out (out should be either 15, or 5)
            cur = ret_amt
            while cur > 0 and (my_bill[5] > 0):
                if cur == 15 and my_bill[10] > 0:
                    cur -= 10
                    my_bill[10] -= 1
                elif my_bill[5] > 0:
                    cur -= 5
                    my_bill[5] -= 1
                
            if cur > 0:
                return False

            # in

            my_bill[bills[i]] += 1

        return True

