class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # progress location
        # sort by from. each car at the from location is active
        # push to location in max heap, so can remove from heap for a given location
        #

        trips_sorted = [ [t[2], t[1], t[0]] for t in trips ]
        # [to, fm, numPassgr] 
        trips_sorted.sort( key = lambda x: x[1] )
#        print( trips_sorted )

        cur_loc = 0
        min_heap = []
        index = 0
        n = len(trips_sorted)
        cur_passgr = 0
        while index < n:
#            print(f'index = {index}, cur_loc = {cur_loc}')
            if trips_sorted[index][1] > cur_loc:
                cur_loc = trips_sorted[index][1]

            while index < n and trips_sorted[index][1] <= cur_loc < trips_sorted[index][0]:
                to, fm, numpass = trips_sorted[index]
                heapq.heappush(min_heap, [to, fm, numpass])
                cur_passgr += numpass
                index += 1                
#                print(f'adding {numpass}, {cur_passgr}')

            
            # remove from 
#            print(f'minheap peek: {min_heap[0]}')
            while min_heap[0][0] <= cur_loc:
                nto, fn, numpass = heapq.heappop(min_heap)
                cur_passgr -= numpass
#                print(f'removing {numpass}, {cur_passgr}')

#            print(f'cur loc = {cur_loc}, numpass = {numpass}')
            if cur_passgr > capacity:
                return False


        return True


