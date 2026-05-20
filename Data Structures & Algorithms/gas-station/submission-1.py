class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
# Input: gas = [1,2,3,4], cost = [2,2,4,1]
# st = 2
# index = (2 + 0) % 4 = 2
# q = gas[2] + 0 = 3 
# cost[2 + 1] = 
#

        n = len(gas)

        def do(i):
            count = 0
            residue = 0
            while count < n:
                index = (i + count) % n
                quantity = gas[index] + residue
                if quantity < cost[ index ]:
                    return False
                else:
                    residue = quantity - cost[ index ]
                    count += 1

            return True


        for i in range(n):
            if do(i):
                return i

        return -1            