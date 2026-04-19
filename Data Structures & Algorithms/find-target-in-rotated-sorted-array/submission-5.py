class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums) - 1

        while l <= u:
            m = u - (u - l) // 2
            if nums[m] == target:
                return m

            if nums[l] == target:
                return l

            if nums[u] == target:
                return u

#            print(f'l = {l}, m = {m}, u ={u}')


            if nums[m] < nums[u]:
                if nums[m] < target <nums[u]:
                    l = m + 1
                else:
                    u = m -1
            else:
                if nums[l] < target <nums[m]:
                    u = m - 1
                else:
                    l = m + 1

        return -1
