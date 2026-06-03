class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        if nums[left] < target:
            left += 1
        
#        print(left, right, mid)
        return left