class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxamt = -1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                tmp = width * height
                if tmp > maxamt:
                    maxamt = tmp

        return maxamt