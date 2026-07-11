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
            # 15 -> 5
            if ret_amt == 15:
                if my_bill[10] >= 1:
                    ret_amt -= 10
                    my_bill[10] -= 1
                elif my_bill[5] >= 2:
                    ret_amt -= 10
                    my_bill[5] -= 2
                else:
                    return False
            # 5 -> 0
            if ret_amt == 5:
                if my_bill[5] == 0:
                    return False

                my_bill[5] -= 1

            # in
            my_bill[bills[i]] += 1

        return True

