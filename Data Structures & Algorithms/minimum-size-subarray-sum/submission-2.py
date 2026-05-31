class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        cur_total = 0
        left = 0
        res = float("infinity")

        for right in range(len(nums)):
            cur_total += nums[right]

            # if cur_total < target: 
            #     continue
            # right = 
#            temp = cur_total
            while cur_total >= target:
                cur_len = right - left + 1
                res = min(res, cur_len)
                cur_total -= nums[left]
                left += 1
            
            # end state: left - 1 gives cur_total >= target, left vilate

        return res if res < float("infinity") else 0

            