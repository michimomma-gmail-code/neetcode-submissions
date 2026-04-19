class Solution:
    def trap0(self, height: List[int]) -> int:
        leftmax = -1
        prefix = [0]
        for i in range(1, len(height)):
            if height[i-1] > leftmax:
                leftmax = height[i-1]
            prefix.append(leftmax)
        

        rightmax = -1
        postfix = [0]
        for i in range(len(height)-2, -1, -1):
            if height[i+1] > rightmax:
                rightmax = height[i+1]
            postfix.append(rightmax)

        postfix = postfix[::-1]
        print(prefix)
        print(postfix)

        res = 0
        for i in range(len(height)):
            area = min(prefix[i],postfix[i]) - height[i]
            if area > 0:
                res += area
        
        return res

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(height[l], leftmax)
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(height[r], rightmax)
                res += rightmax - height[r]
        
        return res


