class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 1

        is_down, is_up = False, False
        cur = 1
        if arr[0] < arr[1]:
            is_up = True
            cur = 2
        if arr[0] > arr[1]:
            is_down = True    
            cur = 2

        max_ts = cur
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                if is_up:
                    cur += 1
                else:
                    cur = 2
                is_up = False
                is_down = True

            elif arr[i] < arr[i + 1]:
                if is_down:
                    cur += 1
                else:
                    cur = 2
                is_down = False
                is_up = True
            else:
                is_down = is_down = False
                cur = 1
#            print(arr[i], cur)
            max_ts = max(max_ts, cur)

        return max_ts