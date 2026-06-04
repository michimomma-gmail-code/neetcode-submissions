class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [2 4 6 1 3 10]
        # [2 6 12 13 16 26]
        # 

        def partition(max_weight):
            i = 0
            cum = 0
            num_partition = 0
            while i < len(weights) and cum < max_weight:
                cum += weights[i]
                if cum == max_weight:
                    cum = 0
                    num_partition += 1
                    i += 1
                elif cum > max_weight:
                    cum = 0            
                    num_partition += 1
                else:
                    i += 1

            if cum > 0:
                num_partition += 1

            if num_partition <= days:
                return True
            else:
                return False  
                
        left, right = max(weights), sum(weights)
        count = 0
        while left < right:
            count += 1
            mid = left + (right - left) // 2
            print(f'mid = {mid}')
            res = partition(mid)
            print(f'res = {res}')
            if res:
                right = mid
            else:
                left = mid + 1
        
        return left