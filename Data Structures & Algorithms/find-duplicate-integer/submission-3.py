class Solution:
    def findDuplicate0(self, nums: List[int]) -> int:
        # [1 2 2 3] vs [1 2 3 3] vs [1 2]
        # 
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                return abs(num)
            nums[abs(num)-1] *= -1

#        print(nums)

        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow