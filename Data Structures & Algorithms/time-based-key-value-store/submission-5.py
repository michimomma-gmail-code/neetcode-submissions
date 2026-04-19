class TimeMap:

    def __init__(self):
        self.kvstore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvstore[key].append( (value, timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        
        def binarySearch(nums, target):
            l, r = 0, len(nums) -1
            print(f'nums = {nums}, target = {target}')
            if target < nums[0][1]:
                return ("", "")

            res = nums[l]
            while l <= r:
                m = r - (r - l) // 2

#                print(f'l = {l}, m = {m}, r = {r}')

                if target >= nums[m][1]:
                    l = m + 1
                else:
                    r = m - 1

                if target >= nums[m][1]:
                    if nums[m][1] >= res[1]:
                        res = nums[m]
            return res
            
        if not key in self.kvstore:
            return ""
        mostRecent = binarySearch(self.kvstore[key], timestamp)
        return mostRecent[0]

