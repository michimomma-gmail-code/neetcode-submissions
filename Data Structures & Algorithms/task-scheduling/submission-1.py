class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        #print(max_heap)
        time = 0

        wait_queue = deque() # (freq, startime)

        while max_heap or wait_queue:
            time += 1

            if max_heap:
                neg_freq = heapq.heappop(max_heap)
                if neg_freq < -1:
                    # remaining task
                    # add to wait que
                    neg_freq += 1
                    wait_queue.append( (neg_freq, time + n) )
#                    heapq.heappush( max_heap, neg_freq )

            if wait_queue:
                start_time = wait_queue[0][1]
                if time == start_time:
                    neg_freq, _ = wait_queue.popleft()
                    heapq.heappush(max_heap, neg_freq)


        return time
