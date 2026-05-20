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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot_gas = sum(gas)
        tot_cost = sum(cost)

        if tot_cost > tot_gas:
            return -1

        
        current_tank = 0
        start_pos = 0
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start_pos = i + 1
                current_tank = 0

        
        return start_pos

