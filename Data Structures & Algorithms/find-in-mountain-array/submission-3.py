class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # 
        n = mountainArr.length()
        if n == 1:
            res = mountainArr.get(0)
            if res == target:
                return 0
            else:
                return -1

        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_val = mountainArr.get(mid)
            mid_val_1 = mountainArr.get(mid + 1)

            if mid_val < mid_val_1: # slope is up. peak is to the right
                left = mid + 1
            else:
                right = mid 

        peak = left
        print(f'peak = {peak}, {mid}, {right}')


#        left, right = 0, peak
        def binSearch(left, right, direction):
            while left <= right:
                mid = left + (right - left) // 2
                val_mid = mountainArr.get(mid)
                if val_mid == target:
                    return mid
                if direction == 1:
                    if val_mid < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if val_mid < target:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1

        res = binSearch(0, peak, 1)
        if res == -1:
            res = binSearch(peak, n - 1, -1)

        return res


