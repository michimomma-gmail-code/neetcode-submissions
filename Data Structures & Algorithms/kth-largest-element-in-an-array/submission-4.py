import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap 
        # push 1st k-th elems
        # for k+1 and beyond
        # if it is larger than minheap[0]
        #   pushpop
        
        minheap = []

        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:

                if minheap[0] < num:
                    heapq.heappushpop(minheap, num)

        
        return minheap[0]



    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [2, <3>, 1, 5, 4]
        # i = 0, lt = 0, gt = 4, p = 3
        #   2 < 3 -> i = 1, lt = 1, gt = 4
        # i = 1, lt = 1, gt = 4, p = 3
        #   3 = 3 -> i = 2, lt = 1, gt = 4
        # i = 2, lt = 1, gt = 4
        #   1 < 3 -> swap [2, 1, <3>, 5, 4], i = 3, lt = 2, gt = 4
        # i = 3, lt = 2, gt = 4
        #   5 > 3 -> swap [2, 1, <3>, 4, 5], i = 4, lt = 2, gt = 3
        # i = 4, lt = 2, ge = 3
        #   5 > 3 -> swap [2, 1, <3>, 5, 4], i = 4, lt = 2, gt = 2

        target = len(nums) - k

        lo, hi = 0, len(nums) - 1


        while True:

            lt, i, gt = lo, lo, hi
            p = nums[random.randint(lo, hi)]
    #        p = 3
#            print(p)
            while i <= gt:
                if nums[i] < p:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > p:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

#            print(f"i = {i}, lt = {lt}, gt = {gt}, {nums}")

            if target < lt:
                hi = lt - 1
            elif target > gt:
                lo = gt + 1
            else:
                return p


    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k

        def select(lo, hi):
            i, lt, gt = lo, lo, hi
            pivot = nums[random.randint(lo, hi)]
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if target_index < lt:
                return select(lo, lt -1)
            elif target_index > gt:
                return select(lt + 1, hi)
            else:
                return pivot

        
        return select(0, len(nums) -1)

        
