class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pt1, pt2 = m - 1, n - 1
        write_ptr = m + n - 1

        res = []
        while 0 <= pt1 < m and 0 <= pt2 < n:
            if nums1[pt1] > nums2[pt2]:
#                res.append(nums1[pt1])
                nums1[write_ptr] = nums1[pt1]
                pt1 -= 1
            else:
#                res.append(nums2[pt2])
                nums1[write_ptr] = nums2[pt2]
                pt2 -= 1

            write_ptr -= 1

        
#        print(nums1, nums2, pt1, pt2)
        if pt2 >= 0:
            nums1[:(pt2 + 1)] = nums2[:(pt2 + 1)]
#            res.append(nums1[:pt1])
