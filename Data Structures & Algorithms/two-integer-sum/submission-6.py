class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {} # num:index
        for i, num in enumerate(nums):
            rest = target - num
            if rest in mem and i > mem[rest]:
                return [mem[rest], i]

            mem[num] = i
    