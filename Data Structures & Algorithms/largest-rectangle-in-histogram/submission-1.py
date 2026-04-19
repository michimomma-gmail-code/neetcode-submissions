class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Input: heights = [7,1,7,2,2,4]
        #Output: 8
        # run through right index
        # [1,2,3]
        #    area continuing -- cannot resolve by the end
        # [3,2,1]
        #    3 resolves when 2 is seen, 2 resolves when 1 is seen
        max_area = 0
        heights.append(0)
        stack = []
        for r, h in enumerate(heights):
            start = r
            #resolve
            while stack and stack[-1][1] > h:
                _l, _h = stack[-1]
                _w = r - _l
                _area = _h * _w
                #print(f'r = {r}, resolving {stack[-1]}, area = {_area}')
                max_area = max(max_area, _area)
                start = _l
                stack.pop()

            stack.append( (start, h) )

        return max_area