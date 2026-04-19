class Solution:
    def maxArea0(self, heights: List[int]) -> int:
        maxamt = -1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                tmp = width * height
                if tmp > maxamt:
                    maxamt = tmp

        return maxamt

    def maxArea(self, heights: List[int]) -> int:
        maxamt = -1
        left = 0
        right = len(heights)-1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            tmp = width * height
            if tmp > maxamt:
                maxamt = tmp
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxamt

