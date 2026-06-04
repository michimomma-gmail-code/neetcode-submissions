class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def maxWeightValid(max_weight):

            cur = 0
            num_ship = 1
            for weight in weights:
                if cur + weight > max_weight:
                    num_ship += 1
                    cur = weight
                else:
                    cur += weight
            
            return num_ship <= days

        left, right = max(weights), sum(weights)
        # binary search
        # feasible region: larger max_weight
        # goal min (max_weight)
        # [False, False, True, True]
        
        while left < right:
            mid = (right + left) // 2
            res = maxWeightValid(mid)
            print(f'mid = {mid}, res = {res}')
            if res:
                right = mid
            else:
                left = mid + 1
        return left


                
            