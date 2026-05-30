class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        def ksum(start_idx, target, k):
            res = []

            if k == 2:
                left, right = start_idx, len(nums) - 1

                while left < right:
                    curr = nums[left] + nums[right]
                    if curr == target:
                        res.append( [nums[left], nums[right]] )
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                    elif curr < target:
                        left += 1
                    else:
                        right -= 1
                return res
            
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue

                cur_target = target - nums[i]

                left, right = i + 1, len(nums) - 1
                for subset in ksum(left, cur_target, k - 1):
                    res.append( [nums[i]] + subset)

            return res

        res = ksum(0, target, 4)
        print(res)

        return res
