import random

class Solution:
    def sortArray0(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        def merge(list1, list2):
            p1, p2 = 0, 0
            res = []
            while p1 < len(list1) and p2 < len(list2):
                if list1[p1] < list2[p2]:
                    res.append(list1[p1])
                    p1 += 1
                else:
                    res.append(list2[p2])
                    p2 += 1

            while p1 < len(list1):
                res.append(list1[p1])
                p1 += 1

            while p2 < len(list2):
                res.append(list2[p2])
                p2 += 1
            
            return res


        def dfs(l, r):
#            print(f'l = {l}, r = {r}')
            if l == r:
                return [nums[l]]
            # if l + 1 == r:
            #     return [min(nums[l], nums[r]), max(nums[l], nums[r])]
            # 1, 5, (6)/2 = 3
            h = (l + r) // 2
            left = dfs(l, h)
            right = dfs(h + 1, r)
#            print(left, right)
            merged = merge(left, right)
#            print(merged)

            return merged

        return dfs(0, len(nums) - 1)

    def sortArray(self, nums: List[int]) -> List[int]:
        # take 1st elem (pivot = 0)
        # partition one >= nums[pivot], the other < nums[pivot]
        # iterate 
        # 
        def _partition(l, r):
            rand_idx = random.randint(l, r)
            nums[r], nums[rand_idx] = nums[rand_idx], nums[r]
            
            pivot = nums[r]
            i = l # index lower partition boundary
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            
            nums[r], nums[i] = nums[i], nums[r]

            return i

        def quickSort(l, r):
            if l >= r:
                return 
            index = _partition(l, r)

            quickSort(l, index - 1)
            quickSort(index + 1, r)

        
        quickSort(0, len(nums) - 1)

        return nums

            