class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter = nums1
        longer = nums2
        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        len_total = len(shorter) + len(longer) 
        half_index = len_total // 2

        is_odd = True if len_total % 2 else False

# example 
#   (m = 0, 1, 2)
#   shorter [1 | 2] m = 0 
#   longer [2 3 | 4 5] 
#.
#   case: [1]
#   [-inf | (1)] m = 0 or [(1) | inf] m = 1
#.  [1 2]
#.  [-inf | 1 2 inf] m = 0, [-inf 1 | 2 inf], m = 1, [-inf 1 2 | inf] m = 2
#   len_total = 6
#   half_index = 3
#   n = half_index - m = 3 - 0 = 3  [-inf | (1) 2], [2 3 4 | (5)] -- m = 0, n = 3
#                      = 3 - 1 = 2. [1 | (2)], [2 3 | (4) 5] -- m = 1, n = 2
#
#   partition_low   [... max(shorter[m-1], longer[n-1])]
#   partition_high  [min(shorter[m], longer[n]), ...]
#
#   validity:  shorter[m - 1] <= longer[n] and longer[n - 1] <= shorter[m]
        l_s = len(shorter)
        h_l = len(longer)

        l, r = 0, l_s

        shorter.append(float('infinity'))
        longer.append(float('infinity'))


        while l <= r:
            m = (l + r) // 2
            n = half_index - m

            if m > 0:
                part_low_s = shorter[m - 1]
            else:
                part_low_s = -float('infinity')
            if n > 0:
                part_low_l = longer[n - 1]
            else:
                part_low_l = -float('infinity')
                
            part_high_s, part_high_l = shorter[m], longer[n]

            if part_low_s <= part_high_l and part_low_l <= part_high_s:
                if not is_odd:
                    return (max(part_low_s, part_low_l) + min(part_high_s, part_high_l)) / 2
                else:
                    return min(part_high_s, part_high_l)
            elif part_low_s > part_high_l:
                u = m - 1
            else:
                l = m + 1

        return -1

