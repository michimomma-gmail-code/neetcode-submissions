class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # t from start time of meetings
        # also, t from end time of the meeting that has started
        # so, t can be
        #       original start time
        #       end time of meeting
        # when there is empty room, start meeting from meeting queue
        # put end time of the meeting into time queue
        # 
        #

        # room: track which room is used (or available)
        #  room_minhash (room_id)
        # start time and [end time] will be updated due to conflict
        # 

        if not meetings:
            return 0

        meetings = sorted(meetings, key = lambda i: i[0])
        rooms_available = [i for i in range(n)]
        heapq.heapify(rooms_available)
        cur = meetings[0]
        rooms_in_use = []
        # (endtime, room id)
        room_id = heapq.heappop(rooms_available)
        heapq.heappush(rooms_in_use, (cur[1], room_id) )
        room_use_count = [0] * n
        room_use_count[room_id] += 1

        for meeting_id in range(1, len(meetings)):
            cur = meetings[meeting_id]
            t_start, t_end = cur[0], cur[1]
            
            # clean up rooms_in_use 
            while rooms_in_use and t_start >= rooms_in_use[0][0]:
                _t, _room_id = heapq.heappop(rooms_in_use)
                heapq.heappush(rooms_available, _room_id)

            if rooms_available:
                # get room id
                room_id = heapq.heappop(rooms_available)
                # add to the rooms_in_use
                heapq.heappush(rooms_in_use, ( t_end, room_id ) )
                room_use_count[room_id] += 1

            else:
                # "wait" until earliest time current meeting is done
                earliest_end_time, used_room_id = heapq.heappop(rooms_in_use)
                # push it to rooms_available
#                heapq.heappush(rooms_available, used_room_id)

                new_t_end = earliest_end_time + (t_end - t_start)
                # push
                heapq.heappush(rooms_in_use, (new_t_end, used_room_id))
                room_use_count[used_room_id] += 1
                 
        print(room_use_count)
        return room_use_count.index(max(room_use_count))

        