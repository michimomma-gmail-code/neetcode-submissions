class Solution:
    def mySqrt(self, x: int) -> int:
        # y = sqrt(x)
        # y * y = x

        # y(left, right)
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2 
            y2 = mid * mid
            if y2 == x:
                return mid
            elif y2 < x:
                left = mid + 1
            else:
                right = mid - 1

        return right