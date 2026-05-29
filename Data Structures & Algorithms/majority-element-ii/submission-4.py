class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
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