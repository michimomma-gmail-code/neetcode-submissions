class Solution:
    def getOrder0(self, tasks: List[List[int]]) -> List[int]:
        
        minheap = []
        for i in range(len(tasks)):
            enq_time, proc_time = tasks[i]
            heapq.heappush(minheap, (enq_time, proc_time, i))
        
        # tasks = [[1,4],[3,3],[2,1]]
        #              [1, 4] -> [2, 1] -> [3, 3]
        # start_time : 1 5 6
        # end_time   : 4 5 8
        # (end_time = start_time + proc_time - 1)
        # process start:
        # end_tiime < enq_time (required)
        # 
        # if end_time >= enq_time:
        # update enq_time to end_time, to reflect prior task end time
        #
        #
        res = []
        end_time = 0
        while minheap:
#            print(minheap)
            enq_time, proc_time, index = minheap[0]
            if end_time < enq_time:
                heapq.heappop(minheap)
                res.append(index)
                end_time = enq_time + proc_time - 1
                continue

            while end_time >= enq_time:
                enq_time, proc_time, index = heapq.heappop(minheap)
                heapq.heappush( minheap, (end_time + 1, proc_time, index) )
            
        return res

    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        sorted_tasks = [ [task[0], task[1], i] for i, task in enumerate(tasks)]
#        print(sorted_tasks)
        sorted_tasks.sort( key = lambda x: x[0] )
#        print(sorted_tasks)
        res = []
        current_time = 0
        n = len(tasks)

        available_heap = []

        task_idx = 0
        while task_idx < n:
            if current_time < sorted_tasks[task_idx][0]:
                current_time = sorted_tasks[task_idx][0]

            while task_idx < n and sorted_tasks[task_idx][0] <= current_time:
                enq_time, proc_time, index = sorted_tasks[task_idx]
                heapq.heappush(available_heap, (proc_time, index))
                task_idx += 1

            proc_time, index = heapq.heappop(available_heap)
            res.append(index)
            current_time += proc_time

        while available_heap:
            proc_time, index = heapq.heappop(available_heap)
            res.append(index)

        return res
