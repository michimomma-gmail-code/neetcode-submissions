import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
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

    def sortArray1(self, nums: List[int]) -> List[int]:
        
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

    def sortArraym(self, nums: List[int]) -> List[int]:

        def _marge(list_1, list_2):
            p1, p2 = 0, 0
            res = []
            while p1 < len(list_1) and p2 < len(list_2):
                if list_1[p1] < list_2[p2]:
                    res.append(list_1[p1])
                    p1 += 1
                else:
                    res.append(list_2[p2])
                    p2 += 1
            
            while p1 < len(list_1):
                res.append(list_1[p1])
                p1 += 1
            while p2 < len(list_2):
                res.append(list_2[p2])
                p2 += 1

            return res


        def margesort(l, r):

            if l == r:
                return [nums[r]]

            mid = l + (r - l) // 2

            res_l = margesort(l, mid)
            res_r = margesort(mid + 1, r)

            res = _marge(res_l, res_r)

            return res

        l, r = 0, len(nums) - 1
        
        return margesort(l, r)




