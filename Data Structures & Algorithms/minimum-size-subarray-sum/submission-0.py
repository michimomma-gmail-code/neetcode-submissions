class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,1,5,1,5,3], target = 10
        # [2, 1, 5, 1, 5]: 14 (right = 4)
        #  increase right (for loop)
        # [2, 1, 5, 1, 5]
        #  left increase to minimize the window (find the current optimal)
        # [5, 1, 5] (left = 3) 
        #  increase right (last)
        # [5, 1, 5, 3]
        #  left
        # [1, 5, 3] 
        #  done

        cur_total = 0
        left = 0
        res = len(nums)
        achieved_target = False
        for right in range(len(nums)):
            cur_total += nums[right]

            if cur_total < target: 
                continue
            # right = 
            achieved_target = True
#            temp = cur_total
            while left <= right and cur_total >= target:
                cur_total -= nums[left]
                left += 1
            
            res = min(res, right - (left - 1) + 1)
            # end state: left - 1 gives cur_total >= target, left vilate

        return res if achieved_target else 0

            