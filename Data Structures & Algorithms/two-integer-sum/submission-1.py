class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find target - nums[i] = nums[j]
        # 1. store nums in hashmap (num -> index: nums_dict)
        # 2. for each i, compute x = target - num[i], and see if exist (x in nums_dict)

        # 1
        nums_dict = {num: i for (i, num) in enumerate(nums)}

        result = []

        for i, num in enumerate(nums):
            x = target - num
            if x in nums_dict and i != nums_dict[x]:
                tmp = (i, nums_dict[x])
                i1, i2 = min(tmp), max(tmp)
                result.append(i1)
                result.append(i2)
                break

        return result