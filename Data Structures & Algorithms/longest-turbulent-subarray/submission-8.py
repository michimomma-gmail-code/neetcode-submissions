class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = 1
        res = 1

        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                up = down + 1
                down = 1
            elif arr[i] > arr[i + 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            res = max(res, down, up)
        
        return res









