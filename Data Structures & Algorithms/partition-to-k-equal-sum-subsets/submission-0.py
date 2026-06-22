class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        target = total // k
        if total == 0 or total % k > 0:
            return False

        n = len(nums)
        slot = [0] * k

        def dfs(i):
            if i == n:
                return True

            for j in range(k):
                if slot[j] + nums[i] > target:
                    continue
                slot[j] += nums[i]
                if dfs(i + 1):
                    return True
                slot[j] -= nums[i]
                if slot[j] == 0:
                    break
            return False

        return dfs(0)

