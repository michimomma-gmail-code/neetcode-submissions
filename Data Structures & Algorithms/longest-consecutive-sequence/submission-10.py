class Solution:
    def longestConsecutive_1(self, nums: List[int]) -> int:
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

    def longestConsecutive(self, nums: List[int]) -> int:
        # use set to store nums
        # for each num, check num+1 is in the set
        if nums == []:
            return 0
        nums_set = set(nums)
        nums = list(nums_set)

        print(nums)

        max_cons = 1

        for num in nums:
            if num -1 in nums_set:
                continue
            inc = 1
            while num + inc in nums_set:
                inc += 1
            if inc > max_cons:
                max_cons = inc
    
        
        return max_cons


