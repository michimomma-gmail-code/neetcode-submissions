import random

class Solution:
    def sortArray0(self, nums: List[int]) -> List[int]:
        
        def partition(l, r):

            rand_idx = random.randint(l, r)
            nums[rand_idx], nums[r] = nums[r], nums[rand_idx]

            pivot = nums[r]

            i = l # where the next smaller element should go

            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]

            return i


        def quick_sort(l, r):
            if l >= r:
                return

            p = partition(l, r)
            quick_sort(l, p - 1)
            quick_sort(p + 1, r)

        l, r = 0, len(nums) - 1
#        print(partition(0, r))
#        print(nums)

        quick_sort(l, r)

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(l, r):

            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]

            lt = l
            gt = r
            j = l

            while j <= gt:
                if nums[j] < pivot:
                    nums[lt], nums[j] = nums[j], nums[lt]
                    lt += 1
                    j += 1
                elif nums[j] > pivot:
                    nums[gt], nums[j] = nums[j], nums[gt]
                    gt -= 1
                else:
                    j += 1

            return (lt, gt)


        def quick_sort(l, r):
            if l >= r:
                return

            lt, gt = partition(l, r)
            quick_sort(l, lt - 1)
            quick_sort(gt + 1, r)

        l, r = 0, len(nums) - 1
#        print(partition(0, r))
#        print(nums)

        quick_sort(l, r)

        return nums
