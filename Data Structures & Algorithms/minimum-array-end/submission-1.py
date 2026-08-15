class Solution:
    def minEnd(self, n: int, x: int) -> int:
 
        res = 0 

        x_bin = [0] * 64
        n_bin = [0] * 64

        for i in range(64):
            x_bin[i] = (x >> i) & 1
            n_bin[i] = ((n - 1) >> i) & 1

        temp = [v for v in x_bin]

        # print('x = ', x_bin)
        # print('n - 1 = ', n_bin)
        idx = 0
        for i in range(64):
            while idx < 64 and x_bin[idx] != 0:
                idx += 1
            temp[idx] = n_bin[i]
#            print('ni ', n_bin[i], ', idx = ', idx)
            idx += 1
            if idx == 64:
                break

        res = 0
        for i in range(len(temp)):
            if temp[i] == 1:
                res += 2 ** i

        return res
