class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def isMaxSumValid(maxSum):
            # can we split the nums while keeping sum of segment <= given maxSum
            # the number of segment should be <= k

            cur = 0
            numSplit = 1
            for num in nums:
                if cur + num > maxSum:
                    numSplit += 1
                    cur = 0
                cur += num

            return numSplit <= k

        
        left, right = max(nums), sum(nums)
        # larger value is feasible
        # False, False, True, True

        while left < right:
            mid = left + (right - left) // 2
            res = isMaxSumValid(mid)
            print(mid, res)
            if res:
                right = mid
            else:
                left = mid + 1

        return left