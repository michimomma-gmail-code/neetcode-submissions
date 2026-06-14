class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {} # num:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mem:
                if i < mem[diff]:
                    return [i, mem[diff]]
                else:
                    return [mem[diff], i]
            mem[num] = i
