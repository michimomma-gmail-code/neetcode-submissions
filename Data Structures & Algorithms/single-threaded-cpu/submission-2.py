class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks[i] = [enqueueTimei, processingTimei]
        # shortest task processing time, smallerst index
        # 
        minheap = []
        max_time = 0
        for i in range(len(tasks)):
            heapq.heappush(minheap, (tasks[i][0], tasks[i][1], i))
            max_time = max_time + tasks[i][1]

        res = []
        end_time = minheap[0][0]
        for time in range(1, max_time + 1):
            if not minheap:
                break

            eq_time, proc_time, index = minheap[0]
            if eq_time > end_time:
                continue

            if eq_time == end_time:
                print(f'eq_time = {eq_time}')
                heapq.heappop(minheap)
                res.append(index)
                end_time += proc_time
                continue

            while eq_time < end_time:
                eq_time, proc_time, index = heapq.heappop(minheap)
                heapq.heappush(minheap, (end_time, proc_time, index))
            
            
            # eq_time, proc_time, index = heapq.heappop(minheap)
            # res.append(index)
            # end_time = end_time + proc_time

        while minheap:
            eq_time, proc_time, index = heapq.heappop(minheap)
            res.append(index)

        return res