# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right  = 1, n
        cache = {}
        while left <= right:
            mid = left + (right - left) // 2
#            print(f'trying {mid}')
            if mid in cache:
                g = cache[mid]
            else:
                g = guess(mid)
                cache[mid] = g
            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        