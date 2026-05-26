class Solution:
    def majorityElement0(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1

        return res

    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        bit = [0] * 32

        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)

        res = 0
        for i in range(32):
            if bit[i] > (n // 2):
                if i < 31:
                    res |= (1 << i)
                else:
                    res -= (1 << 31)

        return res

