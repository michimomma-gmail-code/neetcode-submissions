class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, u = 0, len(nums) - 1
        res = nums[0]
        while l <= u:
            mid = l - ( (l - u) // 2)

            print(f'l = {l}, mid = {mid}, u = {u}, res = {res}')
            res = min(res, nums[mid])

            if nums[l] < nums[u]:
                return min(res, nums[l])
            else:
#                if mid == u:
#                    return nums[u]
                if nums[mid] >= nums[u]:
                    l = mid + 1
                else:
                    u = mid - 1

        return res



    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[0]

        while l < r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid] < nums[r]:
                return nums[l]

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid 

        return nums[l]
























