class Solution:
    def threeSum_0(self, nums: List[int]) -> List[List[int]]:
        #[-2,1,0,-1,1,1,2]
        if nums == []:
            return []

        nums_freq = {}
        for num in nums:
            nums_freq[num] = 1 + nums_freq.get(num, 0)
        
        nums_set = set(nums)
        result = set()
        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                #n2+n1+target = 0
                #target = -(n2+n1)
                target = - (n1 + n2)
                if target in nums_freq:
                    tmp = 0
                    if n1 == target:
                        tmp += 1
                    if n2 == target:
                        tmp += 1
                    if nums_freq[target] <= tmp:
                        continue
                    tmp = [n1,n2,target]
                    tmp.sort()
                    result.add(tuple(tmp))
        return list(result)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        nums.sort()

        nums_count = {}
        for num in nums:
            nums_count[num] = 1 + nums_count.get(num, 0)

        res = []
        for i1 in range(len(nums)):
            n1 = nums[i1]
            nums_count[n1] -= 1
            if i1 and nums[i1] == nums[i1-1]:
                continue

            for i2 in range(i1+1, len(nums)):
                n2 = nums[i2]
                nums_count[n2] -= 1

                if i2 > i1+1 and nums[i2] == nums[i2-1]:
                    continue

                target = -(n1+n2)
                if target in nums_count and nums_count[target] > 0:
                    res.append([n1, n2, target])

            for i2 in range(i1+1, len(nums)):
                nums_count[nums[i2]] += 1
        return res



    