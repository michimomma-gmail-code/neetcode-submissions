class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # Input: mountainArr = [2,4,5,2,1], target = 2
        # 
        # [2,4,5,2,1]
        # left = 2, right = 1, mid = 5 (up, mid, down)
        # left <= target < mid
        # right = mid - 1
        # left = 2, right = 4, mid = 3 (up, mid, up)
        # left <= target < mid
        # right = mid - 1 = 2

        # [5 2 1] (down, mid, down)
        # left = 5, right = 1, mid = 2
        # if left <= target < mid
        # right = mid - 1
        # if mid < target <= right
        # left = mid + 1

        # [1 2 3 <5> 4 2 1]
        # [1 2 7 <5> 4 2 1]
        # [1 2 3 <5> 7 2 1]
        # 

        def findTarget(left, right, direction):
            # assume monotoic increase
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid
                if direction == 1:
                    if mid_val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                if direction == -1:
                    if mid_val < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        n = mountainArr.length()
        if n == 1:
            res = mountainArr.get(0)
            if res == target:
                return 0
            else:
                return -1

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountainArr.get(mid)
            mid_val_1 = mountainArr.get(mid + 1)

            if mid_val < mid_val_1: # slope is up. peak is to the right
                print(left, mid+1)
                res1 = findTarget(left, mid + 1, 1)
                if res1 >= 0:
                    return res1
                left = mid + 1
            else:
                res2 = findTarget(mid, right, -1)
                right = mid - 1

    
        return res2


