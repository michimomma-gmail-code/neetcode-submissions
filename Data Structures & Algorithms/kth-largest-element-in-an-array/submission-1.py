class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep k-largest items in a heap (size k).
        # if a new data is larger than smallest in the heap, push
        # use min heap

        data = nums[:k]
        heapq.heapify(data)

        for i in range(k, len(nums)):
            min_v = data[0]
            num = nums[i]
            if num > min_v:
                heapq.heapreplace(data, num)

        return data[0]