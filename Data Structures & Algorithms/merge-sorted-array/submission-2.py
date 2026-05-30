class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1 3 5 7 0 0] [2 4]
        # [1 2 3 4 5 7]
        # [1 2 3 4 5 7]

        # [2 4 0 0 0] [1 3 5]
        # [2 4 0 4 5] [1 3 5]
        # [2 4 3 4 5]
        # [1 2 3 4 5]

        pt1, pt2 = m - 1, n - 1

        res = []
        while 0 <= pt1 < m and 0 <= pt2 < n:
            if nums1[pt1] > nums2[pt2]:
#                res.append(nums1[pt1])
                nums1[pt1 + pt2 + 1] = nums1[pt1]
                pt1 -= 1
            else:
#                res.append(nums2[pt2])
                nums1[pt1 + pt2 + 1] = nums2[pt2]
                pt2 -= 1
        
        print(nums1, nums2, pt1, pt2)
        if pt2 >= 0:
            nums1[:(pt2 + 1)] = nums2[:(pt2 + 1)]
#            res.append(nums1[:pt1])
