class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # a = 3, b = 4, c = 2
        # b a b a c b a c
        # a = 0, b = 1, c = 5
        # c c b c c 

        max_heap = [ (-a, 'a'), (-b, 'b'), (-c, 'c')]
        max_heap = [ (cnt, char) for cnt, char in max_heap if cnt < 0]
        heapq.heapify( max_heap )

#        print(max_heap)

        res = []
        prev = None

        while max_heap:
#            print(f'max_heap = {max_heap}, prev = {prev}')
            neg_cnt, char = heapq.heappop(max_heap)
            res.append(char)
            neg_cnt += 1
            if prev:
                heapq.heappush( max_heap, prev )
            prev = None

            if neg_cnt < 0:
                prev = ( neg_cnt, char )

#        print(f'prev = {prev}')

        if prev:
            for i in range(len(res)):
                char = res[i]
                if char == prev[1]:
                    res[i] = char * 2
                    prev = (prev[0] + 1, char)
                if prev[0] == 0:
                    break         

        return "".join(res)

