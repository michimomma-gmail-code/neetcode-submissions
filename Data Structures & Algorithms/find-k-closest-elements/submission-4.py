class Solution:
    def findClosestElements0(self, arr: List[int], k: int, x: int) -> List[int]:
        # sliding window
        # find k-closest integers 
        # [2, 4, 5, 8], k = 2, x = 6
        # right: for loop
        #   for each item, compute distance abs(arr[right] - x)
        #   keep k-items in the window.
        #.   - accumulate up to k-items by incrementing right
        #    - after getting k-items, add right while removing left
        #    - at optimal, k-th item should the the real k-th closest item
        #      - it should be either leftmost or rightmost (left most if they are same)
        #
        #    datastructure of the window
        #.   - keep k-closest?
        #.   - need to add and remove 
        #    - track max distance of the k items
        #    - save left and right inde, with max distance, so result can be easiliy retrieved?
        #    
#        left = 0
        max_dist = float("infinity")
        max_index = None
        for right in range(k - 1, len(arr)):
            left = right - k + 1
            right_dist = abs(x - arr[right])
            left_dist = abs(x - arr[left])
            cur_max = max(right_dist, left_dist)
            if cur_max < max_dist:
                max_dist = cur_max
                max_index = (left, right)

        return arr[max_index[0]: max_index[1] + 1]


    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - 1
        minval = float("infinity")
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        
        return arr[left:(right + 1)]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - 1 - (k - 1)
        # left - right
        # 
        def objfun(index):
            return max( abs(arr[index] - x),  abs(arr[index + (k - 1)] - x) ) 

        mid = 0
        while right > left:
            mid = (right + left) // 2
            if abs(arr[mid] - x) <= abs(arr[mid + (k)] - x):
                right = mid 
            else:
                left = mid + 1
        return arr[left: left + (k)]
            

