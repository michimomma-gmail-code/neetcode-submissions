class Solution:
    def candy0(self, ratings: List[int]) -> int:
        n = len(ratings)

        cand = 1
        up = 0
        down = 0
        cum = cand

        for i in range(1, n):
            if ratings[i] == ratings[i - 1]:
                # reset
                cand = 1
                up = 0
                down = 0
                cum += cand
            # up
            elif ratings[i] - ratings[i - 1] > 0:
                cand += 1
                cum += cand

                up += 1
                down = 0

            # down
            else:
                if up > 0:
                    cand = 1
                else:                
                   cand -= 1
                   
                if cand == 0:
                    print(f'cand = {cand}, down = {down}')
                    cand = 1
                    if down == 0:
                        cum += (down + 1)
                    else:
                        cum += (down + 1)

                cum += cand

                up = 0
                down += 1

            print(f'i = {i}, ratings = {ratings[i]}, cand =  {cand}, up = {up}, down = {down}, cum = {cum}')

        return cum

# ratings=[1,3,2,2,1]
#          1 
#          1 2
#          1 2 1
#          1 2 1 1 (tie. add min: 1)
#          1 2 1 1 0 (add 1 up to current index)
#          1 2 1 2 1 (add 1 up to current index)

# ratings=[4,3,5]
#          1
#          1 1     (1)
#          1 1 2 
#          1 + 1 +2 + 1 = 5

# ratings=[2,3,3]
#          1 2
#          1 2 (done), 1
#          1 + 2 + 1 = 4

# ratings=[1,3,2,2,1]
#          1 
#          1 2
#          1 2 1
#          1 2 1 (done)
#                 1 1 (1)
#          1+2+1 + 1 + 1 + 1 = 7


    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        counts = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                counts[i] = counts[i - 1] + 1
        print(counts)

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                counts[i - 1] = max(counts[i] + 1, counts[i - 1])
        
        print(counts)

        return sum(counts)



