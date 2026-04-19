class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, u = 0, len(nums) - 1
        while l <= u:
            mid = l - ( (l - u) // 2)

            print(f'l = {l}, mid = {mid}, u = {u}')

            if nums[l] < nums[u]:
                return nums[l]
            else:
                if mid == u:
                    return nums[u]
                if nums[mid] > nums[u]:
                    l = mid 
                else:
                    u = mid 

        return nums[mid]