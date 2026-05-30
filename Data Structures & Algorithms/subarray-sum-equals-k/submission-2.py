class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cum_hashmap = {}
        cum_hashmap[0] = 1
        cumsum = 0
        res = 0

        for i in range(len(nums)):
            cumsum += nums[i]

            target = cumsum - k

            if target in cum_hashmap:
                res += cum_hashmap[target]

            cum_hashmap[cumsum] = cum_hashmap.get(cumsum, 0) + 1

        return res