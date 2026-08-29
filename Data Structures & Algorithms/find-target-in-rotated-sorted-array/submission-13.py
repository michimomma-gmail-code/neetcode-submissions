class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
# [4 5 6 7 1 2 3]
# 1) [4 5 <6> 7 1 2 3] -- n[left] < n[mid] if n[left] < target < n[mid] -> right = mid -1, else, left = mid + 1
# 2) [4 5 6 7 1 <2> 3] -- n[mid] < n[right] if n[mid] < target < n[right] -> left = mid + 1, else, right = mid - 1
#       
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
#            if nums[left] < nums[mid]:

        return -1

# [6 7 1 <2> 3 4 5]


    def search(self, nums: List[int], target: int) -> int:
        # nums[l] <= target < nums[r] -> normal bin search
        # ow
        # push to the other size, which eventually get us the normal pattern

        def normal_bs(l, r, target):
            print(f'(l, r) = ({l}, {r})')
            # while l <= r:
            #     mid = l + (r - l) // 2
            #     if target == nums[mid]:
            #         return mid
                
            #     if target < nums[mid]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # return -1
            while l < r:
                mid = l + (r - l) // 2
                if target == nums[mid]:
                    return mid
                
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            if nums[l] == target:
                return l
            else:
                return -1

        
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return normal_bs(l, r, target)

        while l <= r:
            # if nums[l] <= target < nums[r]:
            #     return normal_bs(l, r, target)
            
            mid = l + (r - l) // 2
            # if nums[l] <= target < nums[mid]:
            #     return normal_bs(l, mid, target)
            # elif nums[mid] <= target < nums[r]:
            #     return normal_bs(mid, r, target)
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    print(l, mid)
                    return normal_bs(l, mid, target)
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    return normal_bs(mid + 1, r, target)
                else:
                    r = mid

        return -1
            



























