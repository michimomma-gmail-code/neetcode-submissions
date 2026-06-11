class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # tasks[i] = [enqueueTimei, processingTimei]
        # shortest task processing time, smallerst index
        # 
        minheap = []
        res = []

        n = len(tasks)
        current_time = 0

        tasks_sorted = [ [t[0], t[1], i] for i, t in enumerate(tasks) ]
        tasks_sorted.sort( key = lambda x: x[0] )

        # proceed based on enqueTime, and current time
        # push tasks when they are ready at current time

        task_id = 0
        min_heap = []
        while task_id < n or min_heap:

            if not min_heap and tasks_sorted[task_id][0] > current_time:
                current_time = tasks_sorted[task_id][0]

            while task_id < n and tasks_sorted[task_id][0] <= current_time:
                enq_time, proc_time, index = tasks_sorted[task_id]
                heapq.heappush(min_heap, (proc_time, index))
                task_id += 1

            proc_time, index = heapq.heappop(min_heap)
            res.append(index)
            current_time += proc_time
#            task_id += 1

        return res