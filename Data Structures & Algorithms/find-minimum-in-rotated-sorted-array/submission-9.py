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