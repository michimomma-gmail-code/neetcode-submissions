class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        neg_data = [-s for s in stones]
        heapq.heapify(neg_data)

        while len(neg_data) > 1:

            s1 = -heapq.heappop(neg_data) # max
            s2 = -heapq.heappop(neg_data) # 2nd max

            if s1 > s2:
                new_weight = s1 - s2
                heapq.heappush(neg_data, -new_weight)


        return -neg_data[0] if neg_data else 0
