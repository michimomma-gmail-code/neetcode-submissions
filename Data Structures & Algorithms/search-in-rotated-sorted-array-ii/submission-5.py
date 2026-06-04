class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [3 4 4 5 6 1 2 2]
        # if target in [3 4 4 5 6], discard [1 2 2], else discard [3 4 4 5 6]
        # if target in [3 4 4 <5> 6] -- n[left] <= target < n[mid], discard n[mid+1] etc
        # ir target in [1 <2> 2] -- n[mid] < target <= n[right], discard n[mid -1] etc

        # nums=[1 | 0 <1> 1 1]
        #
        # nums=[0 1 1 1 1]
        # nums=[1 0 1 1 1]
        # 

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            if nums[left] <= nums[mid]: #mid in 1st half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif right != mid : #nums[mid] <= nums[right] # mit in 2nd half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                

        return False