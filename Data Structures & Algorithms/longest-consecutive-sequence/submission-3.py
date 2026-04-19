class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # uniquify. sort nums
        # pointer to check the increment (1) and store current max
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort()

        print(nums)

        cur = 0
        max_cons = 1
        cur_cons = 1

        while(cur < len(nums)-1):
            if nums[cur+1] - nums[cur] == 1:
                cur_cons += 1
            else:
                cur_cons = 1
            cur += 1
            if cur_cons > max_cons:
                max_cons = cur_cons

        return max_cons
