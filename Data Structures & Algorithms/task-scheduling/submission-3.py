class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap to find most frequent task
        # task i is run, task i is not ready for n period
        # need data structure to track readiness (hashtable)
        # 

        task_freq = {}
        for task in tasks:
            task_freq[task] = 1 + task_freq.get(task, 0)

        max_heap = [ -freq for freq in task_freq.values() ]
        heapq.heapify(max_heap)

        time = 0
        wait_queue = deque()

        while max_heap or wait_queue:
            time += 1

            if max_heap:
                neg_freq = heapq.heappop(max_heap)
                neg_freq += 1
                if neg_freq < 0:
                    #wait queue
                    wait_queue.append( (neg_freq, time + n) )

            if wait_queue and wait_queue[0][1] == time:
                neg_freq, _ = wait_queue.popleft()
                heapq.heappush(max_heap,  neg_freq)

        return time

        