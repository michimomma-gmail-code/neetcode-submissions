class Solution:
    def majorityElement0(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)

        count1, count2 = 0, 0
        res1 = res2 = None

        for num in nums:

            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            elif count1 == 0:
                res1 = num
                count1 = 1
            elif count2 == 0:
                res2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if res1 == num:
                count1 += 1
            if res2 == num:
                count2 += 1

        res = []
        if count1 > n // 3:
            res.append(res1)

        if count2 > n // 3:
            res.append(res2)

        return res

    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate = {}
        k = 3

        for num in nums:
            if num in candidate:
                candidate[num] = 1 + candidate.get(num, 0)
            elif len(candidate) < k - 1:
                candidate[num] = 1
            else:
                for cnd in list(candidate.keys()):
                    if candidate[cnd] == 1:
                        del candidate[cnd]
                    else:
                        candidate[cnd] -= 1
        
        counts = {}
        for num in nums:
            if num in candidate:
                counts[num] = 1 + counts.get(num, 0)
        
        threshold = len(nums) // k

        print(counts, threshold)

        res = []
        for num in counts:
            if counts[num] > threshold:
                res.append(num)

        return res
