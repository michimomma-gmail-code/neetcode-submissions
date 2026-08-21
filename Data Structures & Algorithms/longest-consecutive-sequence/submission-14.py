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




    def longestConsecutive(self, nums: List[int]) -> int:

        nums_s = set(nums)
        done = set()
        max_len_s = 0
        for num in nums_s:
            if num in done:
                continue            

            n1 = num
            len_s = 0
            while (n1 in nums_s) and (n1 not in done):
                done.add(n1)
                n1 = n1 - 1
                len_s += 1
            n1 += 1
            print(len_s, n1)
            n2 = num + 1
            while (n2 in nums_s) and (n2 not in done):
                done.add(n2)
                n2 = n2 + 1
                len_s += 1
            print('len_s = ', len_s, 'n1 =', n1, 'n2 = ', n2)
            max_len_s = max(max_len_s, len_s)            
        return max_len_s


    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        max_len_s = 0
        seen = set()
        for num in nums_s:
            if num in seen:
                continue
            len_s = 0
            if (num - 1) in nums_s:
                continue

            n1 = num
            n2 = n1
            while n2 in nums_s:
                seen.add(n2)
                n2 += 1
                len_s += 1
            n2 -= 1
            max_len_s = max(max_len_s, len_s)
        return max_len_s































