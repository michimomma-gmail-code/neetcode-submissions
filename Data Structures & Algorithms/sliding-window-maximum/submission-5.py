class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res.append(-heap[0][0])

        for r in range(k, len(nums)):
            # e.g., k = 3, r = 3, window = [2 1 0], l = (1, (2, 3))
            #.             r = 4, window = [(2) 1 0 4], l = (2, (3, 4))
            # when window size = k, add nums[r]
#            n_l = nums[r-k] # -- remove
#            n_r = nums[r] # -- add

            heapq.heappush(heap, (-nums[r], r))
            # remove old ones
            l = r - k # 3 - 3 + 1 = 1
            # k = 5, r = 7, l = 2
#            print(f'l = {l}, {heap[0]}')
            while heap[0][1] <= l:
#                print(f'remove l={l}')
                heapq.heappop(heap)

            res.append(-heap[0][0])

        return res

